from shoulder import Shoulder
from auxiliary import Auxiliary
import matplotlib.pyplot as plt
from point import Point

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
        self.s2.setAng(ang2, self.base_s1.getEndPoint(), ang1, False)
        self.s3.setAng(ang2+ang3, self.s2.getEndPoint(), ang1, True)

    
    def drawAuxilCord(self):
        a1 = Auxiliary(self.base_s1.getStartPoint())
        a2 = Auxiliary(self.s2.getStartPoint())
        a3 = Auxiliary(self.s3.getStartPoint())
        a1.draw(self.ax)
        a2.draw(self.ax)
        a3.draw(self.ax)
