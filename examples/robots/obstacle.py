import math
import pygame

class Circle:
    
    def __init__(self, x, y, r, name=None):
        self.x = x
        self.y = y
        self.r = r
        self.name = name

    def outside(self, xi, yi, ri):
        return self.r + ri  < math.sqrt((self.x-xi)**2 + (self.y-yi)**2)

    def inside(self, xi, yi, ri):
        return self.r > math.sqrt((self.x-xi)**2 + (self.y-yi)**2)

    def distance(self, xi, yi):
        return math.sqrt((self.x-xi)**2 + (self.y-yi)**2)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x),int(self.y)), int(self.r))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Rectangle:

    def __init__(self, x0, y0, x1, y1, name=None):

        assert (x0 <= x1 and y0 <= y1)

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.name = name


    def outside(self, xi, yi, ri):
        return not(self.x0 - ri < xi and xi < self.x1 + ri and self.y0 - ri < yi and yi < self.y1 + ri)

    def inside(self, xi, yi, ri):
        return self.x0 < xi < self.x1 and self.y0 < yi < self.y1

    def distance(self, xi, yi):
        return min(
            math.sqrt((self.x0-xi)**2 + (self.y0-yi)**2),
            math.sqrt((self.x0-xi)**2 + (self.y1-yi)**2),
            math.sqrt((self.x1-xi)**2 + (self.y0-yi)**2),
            math.sqrt((self.x1-xi)**2 + (self.y0-yi)**2)
        )

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect((self.x0, self.y0), (self.x1-self.x0, self.y1-self.y0)))
        
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name