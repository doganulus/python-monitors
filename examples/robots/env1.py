#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import pygame
import networkx as nx
import csv

from robotx import Robot
from obstacle import Circle, Rectangle

from monitors import mtl, regexp

def make_video(screen):

    _image_num = 0

    while True:
        _image_num += 1
        str_num = "000" + str(_image_num)
        file_name = "vid/image" + str_num[-4:] + ".jpg"
        pygame.image.save(screen, file_name)
        # print("In generator ", file_name)  # delete, just for demonstration
        # pygame.time.wait(1000)  # delete, just for demonstration
        yield



pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Courier New', 8)
font2 = pygame.font.SysFont('Courier New', 14)

screen = pygame.display.set_mode((1024, 576))
done = False
is_blue = True

save_screen = make_video(screen)  # initiate the video generator
video = False  # at start: video not active

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


clock = pygame.time.Clock()
count = 0

locations = dict(
    A = Circle(800, 100, 30, "A"),
    B = Circle(700, 500, 30, "B"),
    C = Circle(320, 150, 30, "C"),
    D = Circle(300, 450, 30, "D")
)

predicates = dict(
    notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    notD = lambda robot : not locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    D = lambda robot : locations['D'].inside(robot.state[0], robot.state[1], robot.radius)
)





upper_border = Rectangle(0, 0, 1024, 0)
lower_border = Rectangle(0, 576, 1024, 576)
left_border = Rectangle(0, 0, 0, 576)
right_border = Rectangle(1024, 0, 1024, 576)

wall1 = Rectangle(128, 342, 138, 576)

borders = [upper_border, lower_border, left_border, right_border]

walls = [
    # Rectangle(128, 342, 138, 576), 

    Rectangle(0, 218, 50, 228), # \draw[line width=20] (0, 22.3) -- (5.0, 22.3);
    Rectangle(220, 100, 230, 223), # \draw[line width=20] (22.5, 22.3) -- (22.5, 10.0);
    Rectangle(220, 0, 230, 50), # \draw[line width=20] (22.5, 5.0) -- (22.5, 0);
    Rectangle(100, 218, 405, 228), #\draw[line width=20] (10.0, 22.3) -- (35.0, 22.3) -- (40,17.3) -- (40,0);
    Rectangle(395, 0, 405, 223),

    Rectangle(0, 348, 50, 358), #\draw[line width=20] (0, 35.3) -- (5.0, 35.3);
    Rectangle(100, 348, 405, 358), #\draw[line width=20] (10.0, 35.3) -- (35.0, 35.3) -- (40.0, 40.3) -- (40.0,57.6);
    Rectangle(395, 348, 405, 576), 
    Rectangle(525, 0, 535, 50), #\draw[line width=20] (53.0, 0.0) -- (53.0, 5);
    Rectangle(525, 100, 535, 223), #\draw[line width=20] (53.0, 10.0) -- (53.0, 16.3) -- (58.0, 22.3) -- (92.4, 22.3); 
    Rectangle(525, 218, 924, 228), 
    Rectangle(974, 218, 1024, 228), #\draw[line width=20] (97.4, 22.3) -- (102.4, 22.3);
    Rectangle(525, 358, 535, 576), #\draw[line width=20] (53.0, 57.6) -- (53.0, 40.3) -- (58.0, 35.3) -- (70.0, 35.3);
    Rectangle(525, 348, 700, 358), 
    Rectangle(750, 348, 924, 358), #\draw[line width=20] (75.0, 35.3) -- (92.4, 35.3);
    Rectangle(974, 348, 1024, 358), #\draw[line width=20] (97.4, 35.3) -- (102.4, 35.3);
    Rectangle(795, 353, 805, 576), #\draw[line width=20] (80.0, 57.6) -- (80.0, 35.3);
]

doors = dict(
    D5I = Circle(245, 75, 25, 'D5I'),
    D5O = Circle(205, 75, 25, 'D5O'),
    D6BO = Circle(510, 75, 25, 'D6BO'),
    D6BI = Circle(550, 75, 25, 'D6BI'),
    D4I = Circle(75, 203, 25, 'D4I'),
    D4O = Circle(75, 243, 25, 'D4O'),
    D1O = Circle(75, 333, 25, 'D1O'),
    D1I = Circle(75, 373, 25, 'D1I'),
    D6AI = Circle(949, 203, 25, 'D6AI'),
    D6AO = Circle(949, 243, 25, 'D6AO'),
    D3O = Circle(949, 333, 25, 'D3O'),
    D3I = Circle(949, 373, 25, 'D3I'),
    D2O = Circle(725, 333, 25, 'D2O'),
    D2I = Circle(725, 373, 25, 'D2I'),

    OW1I = Circle(100, 258, 20, 'OW1I'), # \draw[->, line width=20] (16.5, 25.15) -- (28.5, 25.15);
    OW1O = Circle(400, 258, 20, 'OW1O'),
    OW2O = Circle(100, 318, 20, 'OW2O'), # \draw[->, line width=20] (28.5, 31.65) -- (16.5, 31.65);
    OW2I = Circle(400, 318, 20, 'OW2I'), 
    OW3I = Circle(530, 258, 20, 'OW3I'), # \draw[->, line width=20] (16.5, 25.15) -- (28.5, 25.15);
    OW3O = Circle(924, 258, 20, 'OW3O'),
    OW4AO = Circle(530, 318, 20, 'OW4AO'), # \draw[->, line width=20] (28.5, 31.65) -- (16.5, 31.65);
    OW4AI = Circle(700, 318, 20, 'OW4AI'), # \draw[->, line width=20] (28.5, 31.65) -- (16.5, 31.65);
    OW4BO = Circle(750, 318, 20, 'OW4BO'), 
    OW4BI = Circle(924, 318, 20, 'OW4BI'), 
)

areas = dict(
    R1 = dict(location=Rectangle(0, 358, 395, 576, 'R1'),    doors=[doors['D1I'], locations['D']]),
    R2 = dict(location=Rectangle(535, 358, 795, 576, 'R2'),  doors=[locations['B'], doors['D2I']]), 
    R3 = dict(location=Rectangle(805, 358, 1024, 576, 'R3'), doors=[doors['D3I']]), 
    R4 = dict(location=Rectangle(0, 0, 220, 220, 'R4'),      doors=[doors['D5O'], doors['D4I']]), 
    R5 = dict(location=Rectangle(228, 0, 395, 220, 'R5'),    doors=[locations['C'], doors['D5I']]), 
    R6 = dict(location=Rectangle(535, 0, 1024, 220, 'R6'),   doors=[locations['A'], doors['D6AI'], doors['D6BI']]), 

    MM = dict(location=Rectangle(405, 0, 525, 576, 'MM'),    doors=[]), 
    ML = dict(location=Rectangle(0, 228, 100, 348, 'ML'),    doors=[]), 
    MR = dict(location=Rectangle(924, 228, 1024, 348, 'MR'), doors=[]), 

    OW1 = dict(location=Rectangle(120, 228, 400, 288, 'OW1'),   doors=[]),
    OW2 = dict(location=Rectangle(120, 288, 400, 348, 'OW2'),   doors=[]),
    OW3 = dict(location=Rectangle(540, 228, 904, 288, 'OW3'),   doors=[]), 
    OW4A = dict(location=Rectangle(520, 288, 700, 348, 'OW4A'), doors=[]),
    OW4B = dict(location=Rectangle(770, 288, 904, 348, 'OW4B'), doors=[]),
)

G = nx.DiGraph()

G.add_edges_from([(doors['D1I'], doors['D1O']), (doors['D1O'], doors['D1I'])])
G.add_edges_from([(doors['D2I'], doors['D2O']), (doors['D2O'], doors['D2I'])])
G.add_edges_from([(doors['D3I'], doors['D3O']), (doors['D3O'], doors['D3I'])])
G.add_edges_from([(doors['D4I'], doors['D4O']), (doors['D4O'], doors['D4I'])])
G.add_edges_from([(doors['D5I'], doors['D5O']), (doors['D5O'], doors['D5I'])])
G.add_edges_from([(doors['D6AI'], doors['D6AO']), (doors['D6AO'], doors['D6AI'])])
G.add_edges_from([(doors['D6BI'], doors['D6BO']), (doors['D6BO'], doors['D6BI'])])
G.add_edges_from([(doors['D1O'], doors['D4O']), (doors['D4O'], doors['D1O'])])
G.add_edges_from([(doors['D5O'], doors['D4I']), (doors['D4I'], doors['D5O'])])
G.add_edges_from([(doors['D6BI'], doors['D6AI']), (doors['D6AI'], doors['D6BI'])])
G.add_edges_from([(doors['D3O'], doors['D6AO']), (doors['D6AO'], doors['D3O'])])

G.add_edges_from([(doors['OW1I'], doors['OW1O'])])
G.add_edges_from([(doors['OW2I'], doors['OW2O'])])
G.add_edges_from([(doors['OW3I'], doors['OW3O'])])
G.add_edges_from([(doors['OW4AI'], doors['OW4AO'])])
G.add_edges_from([(doors['OW4BI'], doors['OW4BO'])])

G.add_edges_from([(doors['OW1O'], doors['D6BO'])])
G.add_edges_from([(doors['OW4AO'], doors['D6BO'])])
G.add_edges_from([(doors['OW1O'], doors['OW2I'])])
G.add_edges_from([(doors['OW4AO'], doors['OW2I'])])
G.add_edges_from([(doors['OW1O'], doors['OW3I'])])
G.add_edges_from([(doors['OW4AO'], doors['OW3I'])])
G.add_edges_from([(doors['D6BO'], doors['OW3I'])])
G.add_edges_from([(doors['D6BO'], doors['OW2I'])])

G.add_edges_from([(doors['D2O'], doors['OW4AI'])])
G.add_edges_from([(doors['OW4BO'], doors['D2O'])])
G.add_edges_from([(doors['OW4BO'], doors['OW4AI'])])

G.add_edges_from([(doors['OW4BI'], doors['OW4AO'])])

G.add_edges_from([(doors['D1O'], doors['OW1I'])])
G.add_edges_from([(doors['D4O'], doors['OW1I'])])

G.add_edges_from([(doors['D3O'], doors['OW4BI'])])
G.add_edges_from([(doors['D6AO'], doors['OW4BI'])])
G.add_edges_from([(doors['OW3O'], doors['OW4BI'])])
G.add_edges_from([(doors['OW2O'], doors['D4O'])])
G.add_edges_from([(doors['OW2O'], doors['D1O'])])
G.add_edges_from([(doors['OW3O'], doors['D6AO'])])
G.add_edges_from([(doors['OW3O'], doors['D3O'])])

G.add_edges_from([(doors['D2I'], locations['B']), (locations['B'], doors['D2I'])])
G.add_edges_from([(doors['D6AI'], locations['A']), (locations['A'], doors['D6AI'])])
G.add_edges_from([(doors['D6BI'], locations['A']), (locations['A'], doors['D6BI'])])
G.add_edges_from([(doors['D5I'], locations['C']), (locations['C'], doors['D5I'])])
G.add_edges_from([(doors['D1I'], locations['D']), (locations['D'], doors['D1I'])])

G.add_edges_from([(areas['R1']['location'], doors['D1I'])])
G.add_edges_from([(areas['R2']['location'], doors['D2I'])])
G.add_edges_from([(areas['R3']['location'], doors['D3I'])])
G.add_edges_from([(areas['R4']['location'], doors['D4I'])])
G.add_edges_from([(areas['R4']['location'], doors['D5O'])])
G.add_edges_from([(areas['R5']['location'], doors['D5I'])])
G.add_edges_from([(areas['R6']['location'], doors['D6AI'])])
G.add_edges_from([(areas['R6']['location'], doors['D6BI'])])

# G.add_edges_from([(areas['OW1']['location'], doors['OW1O'])])
# G.add_edges_from([(areas['OW2']['location'], doors['OW2O'])])
# G.add_edges_from([(areas['OW3']['location'], doors['OW3O'])])
# G.add_edges_from([(areas['OW4A']['location'], doors['OW4AO'])])
# G.add_edges_from([(areas['OW4B']['location'], doors['OW4BO'])])

nx.drawing.nx_pydot.write_dot(G, "graph.dot")

# routes = nx.all_simple_paths(G, source=doors['D1I'], target=doors['D5I'], cutoff=15)
# print([str(r) for r in routes])

# mission1 = regexp.monitor(

#     "( notA(s)*; A(s); ((notB(s)*; B(s)) | (notC(s)*; C(s))) )+",

#     notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
#     A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
#     notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
#     B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
#     notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
#     C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
#     )

mission1 = regexp.monitor(

    "( notA(s)*; A(s); notB(s)*; B(s) ; notC(s)*; C(s) )+",

    notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    )

mission2 = regexp.monitor(

    "notA(s)*; A(s); (notD(s)*; D(s); notB(s)*; B(s); notC(s)*; C(s) )+",

    notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    notD = lambda robot : not locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    D = lambda robot : locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    )

mission3 = regexp.monitor(

    "(notA(s)*; A(s); notB(s)*; B(s); ((notC(s)*; C(s)) | (notD(s)*; D(s))) )+",

    notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    notD = lambda robot : not locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    D = lambda robot : locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    )

mission4 = regexp.monitor(

    "(notC(s)*; C(s); ((notB(s)*; B(s)) | (notD(s)*; D(s))); notA(s)*; A(s) )+",

    notA = lambda robot : not locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    A = lambda robot : locations['A'].inside(robot.state[0], robot.state[1], robot.radius),
    notB = lambda robot : not locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    B = lambda robot : locations['B'].inside(robot.state[0], robot.state[1], robot.radius),
    notC = lambda robot : not locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    C = lambda robot : locations['C'].inside(robot.state[0], robot.state[1], robot.radius),
    notD = lambda robot : not locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    D = lambda robot : locations['D'].inside(robot.state[0], robot.state[1], robot.radius),
    )

robot1 = Robot(
    mission=mission1, 
    mission_locations=[set([locations['A']]), set(), set([locations['B']]), set(), set([locations['C']]), set(), set([locations['A']])], 
    areas=areas,
    topomap=G, 
    # x=75, y=500, theta=0)
    x=675, y=100, theta=0)

robot2 = Robot(
    mission=mission2, 
    mission_locations=[set([locations['A']]), set(), set([locations['D']]), set(), set([locations['B']]), set(), set([locations['C']]), set(), set([locations['D']])], 
    areas=areas,
    topomap=G, 
    x=875, y=500, theta=0,
    color=GREEN)

robot3 = Robot(
    mission=mission3, 
    mission_locations=[set([locations['A']]), set(), set([locations['B']]), set(), set([locations['C'], locations['D']]), set(), set([locations['A']]),set(), set([locations['A']])], 
    areas=areas,
    route_monitor= mtl.monitor(
        "always((visit1(node) && once visit0(node)) -> (!visit2(node) since visit0(node)))", 
            visit0=lambda node: node.name == 'D1I', 
            visit1=lambda node: node.name == 'A',
            visit2=lambda node: node.name == 'D6BO' or node.name == 'D6BI'
        ),
    topomap=G, 
    x=250, y=500, theta=0,
    color=RED)

robot4 = Robot(
    mission=mission4, 
    mission_locations=[set([locations['C']]), set(), set([locations['B'], locations['D']]), set(), set([locations['A']]), set(), set([locations['A']]),set(), set([locations['C']])], 
    areas=areas,
    topomap=G, 
    x=150, y=100, theta=0,
    color=BLACK)

# robot2 = Robot(
#     mission=mission2, 
#     mission_locations=[0, locations['A'], locations['A'], locations['B'], locations['B'], locations['C'], locations['C']], 
#     areas=areas,
#     topomap=G, 
#     x=875, y=500, theta=0,
#     color=GREEN)

# robot3 = Robot(
#     mission=mission3, 
#     mission_locations=[0, locations['A'], locations['A'], locations['B'], locations['B'], locations['C'], locations['C'],  locations['D'], locations['D']], 
#     areas=areas,
#     topomap=G, 
#     x=250, y=500, theta=0,
#     color=RED)

allrobots = [robot1, robot2, robot3, robot4]

staobs = borders + walls

reddot = Circle(10,10, 6)

for robot in allrobots:
    robot.obstacles = staobs + [reddot] + list(set(allrobots) - set([robot]))




while not done:
    count = count + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: reddot.y -= 3
    if pressed[pygame.K_DOWN]: reddot.y += 3
    if pressed[pygame.K_LEFT]: reddot.x -= 3
    if pressed[pygame.K_RIGHT]: reddot.x += 3
        
    screen.fill(WHITE)
    # pygame.draw.circle(screen, RED, (reddot.x, reddot.y), 6)
    for label, location in locations.items():
        location.draw(screen, (255,255,0))
        screen.blit(font2.render(label, False, (0,0,0)), (location.x, location.y)) 

    for wall in walls:
        wall.draw(screen, BLACK)

    # for label, location in doors.items():
    #     location.draw(screen, GREEN)

    # for label, location in areas.items():
    #     location.draw(screen, GREEN)

    # areas["OW1"]['location'].draw(screen, GREEN)

    reddot.draw(screen, RED)

    robot1.update(0.2)
    robot1.draw(screen, font.render('R', False, WHITE))
    pygame.draw.lines(screen, robot1.color, False, [(s[0], s[1]) for s in robot1.history])
    screen.blit(font2.render(str(robot1.goal[0]), False, robot1.color), (10, 10))
    screen.blit(font2.render(str(robot1.target), False, robot1.color), (50, 10)) 

    robot2.update(0.2)
    robot2.draw(screen, font.render('R', False, WHITE))
    pygame.draw.lines(screen, robot2.color, False, [(s[0], s[1]) for s in robot2.history])
    screen.blit(font2.render(str(robot2.goal[0]), False, robot2.color), (10, 30))
    screen.blit(font2.render(str(robot2.target), False, robot2.color), (50, 30)) 

    robot3.update(0.2)
    robot3.draw(screen, font.render('R', False, WHITE))
    pygame.draw.lines(screen, robot3.color, False, [(s[0], s[1]) for s in robot3.history])
    screen.blit(font2.render(str(robot3.goal[0]), False, robot3.color), (10, 50))
    screen.blit(font2.render(str(robot3.target), False, robot3.color), (50, 50)) 

    robot4.update(0.2)
    robot4.draw(screen, font.render('R', False, WHITE))
    pygame.draw.lines(screen, robot4.color, False, [(s[0], s[1]) for s in robot4.history])
    screen.blit(font2.render(str(robot4.goal[0]), False, robot4.color), (10, 70))
    screen.blit(font2.render(str(robot4.target), False, robot4.color), (50, 70)) 
        
    pygame.display.flip()
    clock.tick(30)

    if video:
        next(save_screen)  # call the generator

with open('robot1.csv', mode='w') as csv_file:
    fieldnames = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for state1, state2, state3, state4 in zip(robot1.history, robot2.history, robot3.history, robot4.history):
        writer.writerow({
            'x1': state1[0]/10.0, 'y1': state1[1]/10.0, 
            'x2': state2[0]/10.0, 'y2': state2[1]/10.0, 
            'x3': state3[0]/10.0, 'y3': state3[1]/10.0, 
            'x4': state4[0]/10.0, 'y4': state4[1]/10.0})
