import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/asserhanafy/session6-task/ros2_ws/install/weather_pkg'
