# Manipulator Simulation
This code provides a simulation of a 3 degree-of-freedom robotic manipulator arm. The arm is divided into three shoulders, each represented by a joint. The simulation calculates the angles between each shoulder, allowing the arm to move in a 3D space.

## Dependencies
The code requires the following dependencies:

- `matplotlib`
- `numpy`

## Usage
The class `Manipulator` simulates the robotic arm, and can be instantiated with a `Point` object to represent the starting position of the arm. Once instantiated, the `draw` method can be called to generate a 3D plot of the arm's current position.

Each shoulder can be controlled by setting the angle of the joint using the `setAng` method.

## Classes
### Point
A class that represents a point in a 3D space. It has three attributes for the x, y, and z coordinates. It has methods for setting and getting the coordinates, and setting a new point using another `Point` object.

### Shoulder
A class that represents a shoulder joint of the robotic arm. It has a length attribute, and joint angles attribute. The start point of the joint and the end point of the joint are also represented by `Point` objects. The class has methods for setting the angle of the joint, getting the joint angles, and getting the start and end points of the joint. It also has methods for drawing the joint and end point in a 3D space.

### Auxiliary
A class that represents an auxiliary coordinate system for a `Point` object. It has attributes for the size of the coordinate system, and `Point` objects representing the x, y, and z axes. The class has a method for setting the angle of rotation, and a method for drawing the coordinate system in a 3D space.

### Manipulator
The main class that represents the robotic arm. It has three `Shoulder` objects representing the three joints of the arm. It also has a `Point` object representing the starting position of the arm, and a `matplotlib` figure for displaying the arm's position. The class has a method for drawing the arm in a 3D space.