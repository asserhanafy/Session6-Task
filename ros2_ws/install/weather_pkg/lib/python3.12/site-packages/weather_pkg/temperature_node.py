#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class TemperatureNode(Node):
    def __init__(self):
        super().__init__("temperature_node")
        self.publisher_ = self.create_publisher(String, "temperature", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Temperature sensor has been started")

    def publish_news(self):
        msg = String()
        msg.data = "25"
        self.publisher_.publish(msg)
        msg.data = "5"
        self.publisher_.publish(msg)
        msg.data = "50"
        self.publisher_.publish(msg)
        msg.data = "150"
        self.publisher_.publish(msg)
        msg.data = "75"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()