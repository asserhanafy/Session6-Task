cmake_minimum_required(VERSION 3.5)
project(weather_pkg)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Add service files
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/data.srv"
)

# Install targets
ament_export_dependencies(rosidl_default_runtime)
ament_package()
