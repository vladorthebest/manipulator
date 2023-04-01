import math
from point import Point
import numpy as np

class Auxiliary:
    size = 50
    def __init__(self, point) -> None:
        self.start_point = Point(0,0,0)
        self.start_point.setPoint(point)

        self.x = Point(
            self.start_point.getX() + self.size,
            self.start_point.getY(),
            self.start_point.getZ()
        )
        self.y = Point(
            self.start_point.getX(),
            self.start_point.getY() + self.size,
            self.start_point.getZ()
        )
        self.z = Point(
            self.start_point.getX(),
            self.start_point.getY(),
            self.start_point.getZ() + self.size
        )
    
    def setAng(self, ang):
        ang = math.radians(ang) #radians
        self.ang = ang
        rotation_matrix = np.array(
            [[1, 0, 0],
            [0, np.cos(ang), -np.sin(ang)],
            [0, np.sin(ang), np.cos(ang)]]
        )

        point = np.array([[self.x.getX()], [self.x.getY()], [self.x.getY()]])

        rotated_point = np.dot(rotation_matrix, point)
        self.x.setX(rotated_point[0][0])
        self.x.setY(rotated_point[1][0])
        self.x.setZ(rotated_point[2][0])


        

    def draw(self, ax):
        ax.plot(
            [self.start_point.getX(), self.x.getX()], 
            [self.start_point.getY(), self.x.getY()],
            [self.start_point.getZ(), self.x.getZ()],
            c = 'red'
        )
        ax.plot(
            [self.start_point.getX(), self.y.getX()], 
            [self.start_point.getY(), self.y.getY()],
            [self.start_point.getZ(), self.y.getZ()],
            c = 'green'
        )
        ax.plot(
            [self.start_point.getX(), self.z.getX()], 
            [self.start_point.getY(), self.z.getY()],
            [self.start_point.getZ(), self.z.getZ()],
            c = 'blue'
        )

