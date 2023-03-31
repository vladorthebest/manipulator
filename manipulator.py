import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x 
        self.y = y 
        self.z = z

    def setX(self, x):
        self.x = x 

    def setY(self, y):
        self.y = y 

    def setZ(self, z):
        self.z = z 

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setPoint(self, newPoint):
        self.x = newPoint.getX() 
        self.y = newPoint.getY() 
        self.z = newPoint.getZ() 

    def __str__(self) -> str:
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)


class Shoulder:
    joint_angles = [0, 0]
    l = 0
    ang = 0

    def __init__(self, l, joint_angles) -> None:
        self.l = l
        self.joint_angles = joint_angles[::]
        self.start_point = Point(0, 0, 0)
        z = self.start_point.getZ() + l
        self.end_point = Point(0, 0, z )


    def setAng(self, ang, start_point):
        ang = 90 - ang #degrees
        ang = math.radians(ang) #radians
        self.ang = ang
        self.start_point.setPoint(start_point)

        newX = self.start_point.getX()
        newY = self.start_point.getY() + self.l * math.cos(ang)
        newZ = self.start_point.getZ() + self.l * math.sin(ang)
        self.end_point.setX(newX)
        self.end_point.setY(newY)
        self.end_point.setZ(newZ)

        

    def getEndPoint(self):
        return self.end_point

    def draw(self, ax):
        ax.plot(
            [self.start_point.getX(), self.end_point.getX()], 
            [self.start_point.getY(), self.end_point.getY()],
            [self.start_point.getZ(), self.end_point.getZ()],
        )


class Manipulator:

    start_point = Point(0, 0, 0)
    
    fig = plt.figure()

    
    def __init__(self, point) -> None:
        self.base_s1 = Shoulder(203, [0, 0])
        self.s2 = Shoulder(178, [0, 0])
        self.s3 = Shoulder(178, [0, 0])
        self.start_point.setPoint(point)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 400)
    
    def draw(self):

        self.base_s1.draw(self.ax)  
        self.s2.draw(self.ax)
        self.s3.draw(self.ax)

        plt.show()

    def setAngl(self, ang1, ang2, ang3):
        self.s2.setAng(ang2, self.base_s1.getEndPoint())
        self.s3.setAng(ang2+ang3, self.s2.getEndPoint())
    

man = Manipulator(Point(0, 0, 0))
man.setAngl(0, 45, 30)
man.draw()





