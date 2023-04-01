from point import Point
from manipulator import Manipulator


def main():
    man = Manipulator(Point(0, 0, 0))
    for i in range(-55, 125, 5):
            man.setAngl(0, i, 0)    
            man.drawAnimEndPoints()


if __name__ == "__main__":
    
    main()
