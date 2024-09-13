#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from weather_pkg.srv import SendSensorData

class Station(Node):
    def __init__(self):
        super().__init__("remote_station_node")
        self.srv=self.create_service(SendSensorData,"send_sensor_data",self.check_data)
        self.get_logger.info("station node has started and waiting for data")

    def check_data(self,request,response):
        temp=request.data[0]   
        humidity=request.data[1]
        pressure=request.data[2] 

        self.get_logger().info("Data is received")       

        if(temp<10 or temp>100):
            self.get_logger().info(f"Inavlid Temperature:{temp}")
        else:
            self.get_logger().info(f"Temperature:{temp}")    

        if(temp<0.95 or temp>1.2):
            self.get_logger().info(f"Inavlid Pressure:{pressure}atm")
        else:
            self.get_logger().info(f"Pressure:{pressure}atm") 

        if(humidity<0.7 or temp>0.95):
            self.get_logger().info(f"Inavlid Humidity:{humidity}")
        else:
            self.get_logger().info(f"Humidity:{humidity}")           
        

        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = Station()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()