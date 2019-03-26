#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np
import random


import pygame
import networkx as nx

from itertools import islice
from obstacle import Circle, Rectangle

from monitors import mtl, regexp

# argmax = lambda iterable, func: max(iterable, key=func)


class Robot():

    # Properties
    max_speed = 30.0  # [cm/s]
    min_speed = 0  # [cm/s]
    max_yawrate = 120.0 * math.pi / 180.0  # [rad/s]
    max_accel = 10  # [cm/ss]
    max_dyawrate = 180.0 * math.pi / 180.0  # [rad/ss]
    v_reso = 0.75  # [cm/s]
    yawrate_reso = 12 * math.pi / 180.0  # [rad/s]
    time_reso = 0.3  # [s]
    predict_time = 2.0  # [s]
    obstacle_cost_gain = 1925.0 #600
    to_goal_cost_gain = 1.0 #0.3
    speed_cost_gain = 0.01
    radius = 6  # [cm]

    # Cosmetics
    color = (0, 128, 255) # Blue

    def __init__(self, mission, mission_locations, areas, topomap=None, x=0.0, y=0.0, theta=math.pi, v=0.0, vr=0.0, safety_monitor=None, route_monitor=None, color=(0, 128, 255)):
        self.state = np.array([x, y, theta, v, vr])
        self.areas = areas

        for area in self.areas.values():
            if area['location'].inside(self.state[0], self.state[1], self.radius):
                self.sources = area['doors'] 

        self.trajectories = []
        self.obstacles = []
        self.others = []
        self.best_traj = [(x,y)]
        self.history = [(x,y)]
        self.color = color
        

        self.mission = mission
        self.mission_locations = mission_locations
        self.topomap = topomap
        self.goal = nx.astar_path(self.topomap, self.sources[0], self.sources[0], lambda c1, c2: math.sqrt((c1.x-c2.x)**2 + (c1.y-c2.y)**2))

        self.mission_goals = set()
        for i in range(len(self.mission.states)):
            if self.mission.states[i]:
                self.mission_goals = self.mission_goals.union(self.mission_locations[i])
        self.target = random.choice(list(self.mission_goals))


        if safety_monitor == None:
            self.safety_monitor = mtl.monitor(
                """
                safe(x,y) and
                (inside_eastway(x,y) implies (going_east(theta) since (inside_eastway(x,y) and not(pre(inside_eastway(x,y)))))) and 
                (inside_westway(x,y) implies (going_west(theta) since (inside_westway(x,y) and not(pre(inside_westway(x,y))))))
                """, 
                safe=self.safe,
                inside_eastway=lambda x,y: self.areas["OW1"]['location'].inside(x,y, self.radius) or self.areas["OW3"]['location'].inside(x,y, self.radius),
                going_east=lambda theta: -math.pi/4 <= math.atan2(math.sin(theta), math.cos(theta)) <= math.pi/4,
                inside_westway=lambda x,y: self.areas["OW2"]['location'].inside(x,y, self.radius) or self.areas["OW4A"]['location'].inside(x,y, self.radius) or self.areas["OW4B"]['location'].inside(x,y, self.radius),
                going_west=lambda theta: (math.atan2(math.sin(theta), math.cos(theta)) <= -3*math.pi/4) or (math.atan2(math.sin(theta), math.cos(theta)) >= 3*math.pi/4)
                )
        else:
            self.safety_monitor = safety_monitor 

        self.safety_monitor_init = self.safety_monitor.states.copy()

        if route_monitor == None:
            self.graph_monitor = mtl.monitor("true(node)", true=lambda node: True) 
        else:
            self.graph_monitor = route_monitor

        self.graph_monitor_init = self.graph_monitor.states.copy()

    def motion(self, dt, *u):

        self.state[2] += u[1] * dt
        self.state[0] += u[0] * math.cos(self.state[2]) * dt
        self.state[1] += u[0] * math.sin(self.state[2]) * dt
        
        self.state[3] = u[0]
        self.state[4] = u[1]

        print(self.state[2])


        return self.state

    def predict(self, x, y, theta, v, vr, dt):

        xn = x + v * math.cos(theta) * dt
        yn = y + v * math.sin(theta) * dt
        thetan = theta + vr * dt

        return xn, yn, thetan

    def draw(self, screen, text):
        pos = (int(self.state[0]), int(self.state[1]))

        for traj in self.trajectories:
            pygame.draw.lines(screen, (196, 255, 196), False, [(data[0], data[1]) for data in traj])

        if len(self.best_traj) > 1:
            pygame.draw.lines(screen, (100, 255, 100), False, [(data[0], data[1]) for data in self.best_traj], 4)

        pygame.draw.line(screen, (0, 0, 0), pos, (pos[0] + 20 * math.cos(self.state[2]), pos[1] + 20 * math.sin(self.state[2])), 3)
        pygame.draw.circle(screen, self.color, pos, self.radius)
        screen.blit(text, (pos[0], pos[1])) 



    def calc_trajectory(self, v, vr, predict_time):

        x, y, theta = self.state[0], self.state[1], self.state[2]

        traj = [(x,y,v)]

        time = 0

        self.safety_monitor.states = self.safety_monitor_init.copy()
        self.safety_monitor.prev_states = self.safety_monitor_init.copy()

        while time <= predict_time:
            x, y, theta = self.predict(x, y, theta, v, vr, self.time_reso)

            
            if not self.safety_monitor.update(x=x, y=y, theta=theta):
                return traj, False

            traj.append((x,y,v))
            time += self.time_reso


        return traj, True


    def get_controls(self):

        self.next_control = self.state[3]*0, self.state[4]

        self.trajectories = []

        min_cost = float("inf")

        dw = self.dynamic_window()     
        for v in np.arange(dw[0], dw[1], self.v_reso):
            for vr in np.arange(dw[2], dw[3], self.yawrate_reso):
                for predict_time in [1.0, self.predict_time]:
                    traj, safe = self.calc_trajectory(v, vr, predict_time)
                    if safe:
                        self.trajectories.append(traj)
                    else:
                        break

                    obs_cost = self.obstacle_cost_gain/self.min_safe_distance(traj)
                    speed_cost = self.speed_cost_gain * (self.max_speed - traj[-1][2])

                    if len(self.goal) > 0:
                        # goal_cost = self.to_goal_cost_gain * self.goal[0].distance(traj[-1][0], traj[-1][1])
                        goal_cost = self.calc_to_goal_cost(traj, self.goal[0])  + self.goal[0].distance(traj[-1][0], traj[-1][1])
                    else:
                        goal_cost = 0


                    final_cost =  speed_cost + obs_cost + goal_cost
                    # print(final_cost)

                    if min_cost >= final_cost:
                        min_cost = final_cost
                        self.next_control = [v, vr]
                        self.best_traj = traj

        if self.goal[0].inside(self.state[0], self.state[1], self.radius) and len(self.goal) > 1:
            self.goal = self.goal[1:]
            self.previous_goal = self.goal[0]


        if min_cost == float("inf"):
            print("No safe trajectory", dw, len(np.arange(dw[0], dw[1], self.v_reso)), len(np.arange(dw[2], dw[3], self.yawrate_reso)))

        return self.next_control

    def dynamic_window(self):

        # Dynamic window from robot specification
        Vs = [self.min_speed, self.max_speed,
              -self.max_yawrate, self.max_yawrate]

        # Dynamic window from motion model
        Vd = [self.state[3] - self.max_accel * self.time_reso,
              self.state[3] + self.max_accel * self.time_reso,
              self.state[4] - self.max_dyawrate * self.time_reso,
              self.state[4] + self.max_dyawrate * self.time_reso]

        #  [vmin,vmax, yawrate min, yawrate max]
        dw = [max(Vs[0], Vd[0]), min(Vs[1], Vd[1]),
              max(Vs[2], Vd[2]), min(Vs[3], Vd[3])]
        #  print(dw)

        return dw

    def calc_to_goal_cost(self, traj, goal):
        # calc to goal cost. It is 2D norm.

        relgoal = (goal.x - self.state[0], goal.y - self.state[1])
        reltraj = (traj[-1][0] - self.state[0], traj[-1][1] - self.state[1])

        goal_magnitude = math.sqrt(relgoal[0]**2 + relgoal[1]**2)
        traj_magnitude = math.sqrt(reltraj[0]**2 + reltraj[1]**2)
        dot_product = (relgoal[0] * reltraj[0]) + (relgoal[1] * reltraj[1])
        error = dot_product / (goal_magnitude * traj_magnitude)
        error_angle = math.acos(error)
        cost = self.to_goal_cost_gain * error_angle

        return cost

    def min_safe_distance(self, traj):

        min_r = 100.0
        for x, y, v in traj:
            for obstacle in self.obstacles:
                r = obstacle.distance(x,y) + 2

            if r < min_r:
                min_r =r

        return min_r

    def safe(self, x, y):

        for obstacle in self.obstacles + self.others:
            if not obstacle.outside(x, y, self.radius + 2):
                return False

        return True

    def inside_eastway(self, x, y):
        return self.areas["OW1"]['location'].inside(x,y, self.radius) or self.areas["OW3"]['location'].inside(x,y, self.radius)
    def inside_westway(self, x, y):
        return False

    def outside(self, xi, yi, ri):
        return self.radius + ri < math.sqrt((self.state[0]-xi)**2 + (self.state[1]-yi)**2)

    def distance(self, xi, yi):
        return math.sqrt((self.state[0]-xi)**2 + (self.state[1]-yi)**2)

    def update(self, dt):

        for area in self.areas.values():
            if area['location'].inside(self.state[0], self.state[1], self.radius):
                self.sources = area['doors'] 

        self.mission.update(s=self)

        # print(self.mission.states, self.mission_goals)

        if self.mission.states != self.mission.prev_states:
            self.mission_goals = set()
            for i in range(len(self.mission.states)):
                if self.mission.states[i]:
                    self.mission_goals = self.mission_goals.union(self.mission_locations[i])

            if len(self.mission_goals) > 0:
                self.target = random.choice(list(self.mission_goals))
            
            for path in nx.shortest_simple_paths(self.topomap, self.sources[0], self.target):
                result = True
                for n in path:
                    result = self.graph_monitor.update(node=n)

                self.graph_monitor.states = self.graph_monitor_init.copy()
                self.graph_monitor.prev_states = self.graph_monitor_init.copy()

                print(self.graph_monitor.states)

                if result:
                    print("Route:", path)
                    self.goal = path
                    break


        v, vr = self.get_controls()
        self.motion(dt, v, vr)

        self.history.append((self.state[0], self.state[1]))


