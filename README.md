# My Robot ROS2 Package

A simple ROS2 Humble robotic arm package with:
- URDF model
- Publisher/subscriber examples
- RViz2 visualization

## Structure

- `urdf/` → robot description
- `my_robot/` → Python ROS2 nodes

## Run Robot State Publisher

```bash
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(cat urdf/robotic_arm.urdf)"
