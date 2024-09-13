#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from weather_pkg.srv import Data
# from functools import partial


class Aggregator(Node):
    def __init__(self):
        super().__init__('aggergator_node')
        self.temp_sub=self.create_subscription(String,"temperature",self.temp_callback,10)
        self.humidity_sub=self.create_subscription(String,"humidity",self.humidity_callback,10)
        self.pressure_sub=self.create_subscription(String,"pressure",self.pressure_callback,10)

        self.temp=0
        self.humidity=0
        self.pressure=0

        self.client = self.create_client(Data, 'send_data')  
        while not self.client.wait_for_service(1.0):
            self.get_logger().info('Waiting for remote station service...')

        self.get_logger().info("Aggregator node started and waiting for sensor data...")


    def temp_callback(self,msg):
        self.temp=msg.data 
        self.send_data()

    def humidity_callback(self,msg):
        self.humidity=msg.data
        self.send_data()

    def pressure_callback(self,msg):
        self.pressure=msg.data
        self.send_data()


    def send_data(self):
        if self.temp and self.humidity and self.pressure:
            self.get_logger().info(f"Aggregated Data: Temperature={self.temperature}, Humidity={self.humidity}, Pressure={self.pressure}")

        request = Data.Request()
        request.data = [self.temp, self.humidity, self.pressure]   
        # request=AddThreeInts.Request()
        # request.a=int(float(self.temp))        
        # request.b=int(float(self.pressure))
        # request.c=int(float(self.humidity))

        future=self.client.call_async(request)
        future.add_done_callback(self.callback_response)

        self.temp=0
        self.humidity=0
        self.pressure=0

    def callback_response(self,future):
        try:
            response=future.result()  
            if response.success:
                self.get_logger().info("Sensor data sent successfully!")
            else:
                self.get_logger().error("Failed to send sensor data.")
        except Exception as e:
            self.get_logger().error(f"Failed to send data to remote station: {str(e)}")    

def main(args=None):
    rclpy.init(args=args)
    node = Aggregator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

