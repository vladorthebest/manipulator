from point import Point
from manipulator import Manipulator


def main():
    man = Manipulator(Point(0, 0, 0))
    # man.setAngl(-90, 90, 0)
    # man.draw()
    # for i in range(0, 150, 10):
    #     man.setAngl(-90, 125, i)    
    #     # man.drawAnimEndPoints()
    #     man.drawEndPoints()
    
    for i in range(-90, 90, 10):
        for j in range(-55, 125, 10):
            man.setAngl(i, j, 0)    
            man.drawEndPoints()
    


    # for i in range(0, 150, 10):
    #     man.setAngl(90, 125, i)    
    #     # man.drawAnimEndPoints()
    #     man.drawEndPoints()
    man.showPlot()


if __name__ == "__main__":
    
    main()
