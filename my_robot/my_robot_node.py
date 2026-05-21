#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyRobot(Node):
    def __init__(self):
        super().__init__('my_robot')
        self.get_logger().info('My Robot Node has started!')

def main(args=None):
    rclpy.init(args=args)
    node = MyRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()