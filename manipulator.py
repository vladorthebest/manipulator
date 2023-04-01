import matplotlib.pyplot as plt
import math
import numpy as np

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


    def setAng(self, ang, start_point, ang_base):
        ang = 90 - ang #degrees
        ang = math.radians(ang) #radians
        self.ang = ang
        ang_base = math.radians(ang_base) #radians
        self.ang_base = ang_base
        self.start_point.setPoint(start_point)

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
        # ax.plot(self.end_point.getX(), self.end_point.getY(), self.end_point.getZ(), c='red')


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


class Manipulator:

    start_point = Point(0, 0, 0)
    
    base_s1 = Shoulder(203, [-90, 90])
    s2 = Shoulder(178, [-55, 125])
    s3 = Shoulder(178, [0, 150])
    
    def __init__(self, point) -> None:
        self.fig = plt.figure()
        self.start_point.setPoint(point)
        self.ax = self.fig.add_subplot(111, projection='3d')
        
    

    def draw(self):
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 600)
        
        self.base_s1.draw(self.ax)  
        self.s2.draw(self.ax)
        self.s3.draw(self.ax)
        plt.show()
        
    
    def drawAnim(self):
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 600)
        
        self.base_s1.draw(self.ax)  
        self.s2.draw(self.ax)
        self.s3.draw(self.ax)
        plt.draw()
        plt.pause(0.02)
        self.ax.cla()


    def drawAnimEndPoints(self):
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 600)
        
        
        
        self.s3.drawEndPoint(self.ax)
        self.fig.canvas.draw()
        plt.pause(0.02)
        
    def drawEndPoints(self):
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_xlim(-400, 400)
        self.ax.set_ylim(-400, 400)
        self.ax.set_zlim(0, 600)
        self.s3.drawEndPoint(self.ax)
        

    def showPlot(self):
        plt.show()

    def setAngl(self, ang1, ang2, ang3):
        if(ang1 < self.base_s1.getJoinAngl()[0] or ang1 > self.base_s1.getJoinAngl()[1]):
            print("Invalid angle 1")
            print("Enable: [" + str(self.base_s1.getJoinAngl()[0]) + ":" + str(self.base_s1.getJoinAngl()[1]) + "]")
            return 0
        if(ang2 < self.s2.getJoinAngl()[0] or ang2 > self.s2.getJoinAngl()[1]):
            print("Invalid angle 2")
            print("Enable: [" + str(self.s2.getJoinAngl()[0]) + ":" + str(self.s2.getJoinAngl()[1]) + "]")
            return 0
        if(ang3 < self.s3.getJoinAngl()[0] or ang3 > self.s3.getJoinAngl()[1]):
            print("Invalid angle 3")
            print("Enable: [" + str(self.s3.getJoinAngl()[0]) + ":" + str(self.s3.getJoinAngl()[1]) + "]")
            return 0
        self.s2.setAng(ang2, self.base_s1.getEndPoint(), ang1)
        self.s3.setAng(ang2+ang3, self.s2.getEndPoint(), ang1)

    
    def drawAuxilCord(self):
        a1 = Auxiliary(self.base_s1.getStartPoint())
        a2 = Auxiliary(self.s2.getStartPoint())
        a3 = Auxiliary(self.s3.getStartPoint())
        a1.draw(self.ax)
        a2.draw(self.ax)
        a3.draw(self.ax)

def main():
    man = Manipulator(Point(0, 0, 0))
    for i in range(-55, 125, 5):
            man.setAngl(0, i, 0)    
            man.drawAnimEndPoints()


if __name__ == "__main__":
    
    main()
