
# Hardware Setup

This document describes the hardware components and configurations used for the IE4060 Robotics and Intelligent Systems assignment.

## 1. Components
- **Robot Platform**: TurtleBot3 (Burger/Waffle)
- **Sensors**:
  - Lidar Sensor: Used for mapping the maze and obstacle detection.
  - Camera Module: Used for slit detection on the wall.
  - Ultrasonic Sensors: For proximity detection and precise stopping.
- **Processing Unit**: Raspberry Pi 4 or NVIDIA Jetson Nano for running the algorithms.
- **Motor Driver**: DC motor driver module to control wheel movements.

## 2. Connections
- Connect the Lidar sensor to the robot's USB port.
- Attach the camera module to the top of the robot for an unobstructed view of the wall.
- Ensure the ultrasonic sensors are mounted at the front and sides of the robot.

## 3. Software Setup
- **Operating System**: Ubuntu 20.04 with ROS Noetic installed.
- **Dependencies**:
  - `rospy`: For writing ROS nodes.
  - `OpenCV`: For image processing tasks (slit detection).
  - `numpy`: For numerical computations.
  - `matplotlib`: For visualizing data (optional).
- **Communication**: Ensure ROS master is running, and the robot is connected to the same network as the processing unit.

## 4. Calibration
- Calibrate the Lidar sensor to ensure accurate distance measurements.
- Test the camera feed to adjust the angle and focus for optimal slit detection.
- Adjust PID controller parameters for smooth navigation and precise stopping.

## 5. Testing
- Verify all sensors are working by running individual ROS nodes.
- Test the motor drivers by moving the robot forward, backward, and in rotations.

## Troubleshooting
- If the robot is unresponsive, check the battery level and connections.
- For ROS-related errors, restart the `roscore` and ensure all nodes are active.

## Notes
- The robot should be fully charged before the demonstration.
- Keep a backup SD card with the pre-installed software in case of corruption.
