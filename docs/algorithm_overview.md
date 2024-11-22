
# Algorithm Overview

This document provides a detailed explanation of the algorithms implemented for the IE4060 Robotics and Intelligent Systems assignment. 

## 1. Maze Solving Algorithm
The robot autonomously navigates through a maze to find the exit point. The width of the paths ensures safe navigation for the robot.

### Algorithm: Depth-First Search (DFS)
- **Input**: A grid representation of the maze.
- **Process**:
  1. Start from the initial position of the robot.
  2. Mark the current cell as visited.
  3. Explore all possible directions (North, East, South, West) recursively until the exit is found.
  4. Backtrack if a dead-end is encountered.
- **Output**: The shortest path to the maze exit.

---

## 2. Slit Detection
After exiting the maze, the robot encounters a wall with three slits, which may open or close randomly. The task is to identify the number of open slits.

### Algorithm: Image Processing with Sensors
- **Input**: Sensor data or camera feed from the robot's front view.
- **Process**:
  1. Scan the wall as the robot navigates parallel to it.
  2. Detect gaps (open slits) based on sensor readings or image segmentation.
  3. Count the number of detected slits.
- **Output**: The total number of open slits.

---

## 3. Path Selection Based on Slit Count
The robot must choose a pre-programmed path corresponding to the number of open slits detected.

### Algorithm: Conditional Path Selection
- **Input**: Number of open slits.
- **Process**:
  1. Map slit counts to specific paths:
     - 1 Open Slit → Path 1
     - 2 Open Slits → Path 2
     - 3 Open Slits → Path 3
  2. Execute the trajectory for the selected path using predefined waypoints.
- **Output**: The robot navigates to the parking zone via the selected path.

---

## 4. Stopping in the Parking Zone
The robot must accurately stop within a marked parking zone at the end of the selected trajectory.

### Algorithm: PID Controller for Precise Stopping
- **Input**: Position feedback from sensors.
- **Process**:
  1. Use the PID controller to adjust the robot's speed as it approaches the parking zone.
  2. Ensure the robot stops within the marked area.
- **Output**: Robot halts in the correct position.

---

## Enhancements
- **Optimization**: Added checks to avoid redundant path exploration during maze solving.
- **Error Handling**: Implemented robust slit detection to handle variable lighting conditions.

## Conclusion
The combination of these algorithms ensures smooth navigation, accurate slit detection, and proper path selection, allowing the robot to complete its tasks effectively.
