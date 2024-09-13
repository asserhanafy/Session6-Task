import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danya-ahmed/session6-task/ros2_ws/src/weather_pkg/install/weather_pkg'
