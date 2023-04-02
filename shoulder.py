import math
from point import Point

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


    def setAng(self, ang, start_point, ang_base, revers):
        ang = 90 - ang #degrees
        ang = math.radians(ang) #radians
        self.ang = ang
        ang_base = math.radians(ang_base) #radians
        self.ang_base = ang_base
        self.start_point.setPoint(start_point)

        if ang_base<0 and revers:
            newX = (self.start_point.getX() - self.l * math.cos(ang))*math.sin(ang_base)*(-1)
        else:
            newX = (self.start_point.getX() + self.l * math.cos(ang))*math.sin(ang_base)
        newY = (self.start_point.getY() + self.l * math.cos(ang))*math.cos(ang_base)
        newZ = self.start_point.getZ() + self.l * math.sin(ang)
        self.end_point.setX(newX)
        self.end_point.setY(newY)
        self.end_point.setZ(newZ)
    

    def getJoinAngl(self):
        return self.joint_angles   

    def getEndPoint(self):
        return self.end_point

    def getStartPoint(self):
        return self.start_point

    def draw(self, ax):
        ax.plot(
            [self.start_point.getX(), self.end_point.getX()], 
            [self.start_point.getY(), self.end_point.getY()],
            [self.start_point.getZ(), self.end_point.getZ()],
            c = 'hotpink'
        )
    
    def drawEndPoint(self, ax):
        ax.scatter(self.end_point.getX(), self.end_point.getY(), self.end_point.getZ(), c='red')
        

