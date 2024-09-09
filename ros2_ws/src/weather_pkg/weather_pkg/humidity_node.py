#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class HumidityNode(Node):
    def __init__(self):
        super().__init__("humidity_node")
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Humidity sensor has been started")

    def publish_news(self):
        msg = String()
        msg.data = "0.8"
        self.publisher_.publish(msg)
        msg.data = "0.6"
        self.publisher_.publish(msg)
        msg.data = "0.9"
        self.publisher_.publish(msg)
        msg.data = "1.0"
        self.publisher_.publish(msg)
        msg.data = "0.95"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HumidityNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()