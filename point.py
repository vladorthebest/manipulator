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

