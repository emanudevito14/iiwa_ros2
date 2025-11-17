Put iiwa_ros2 (updated with aruco_tag) and [aruco_ros](https://github.com/pal-robotics/aruco_ros)
 in ros2_ws/src.
 ```
git clone https://github.com/emanudevito14/iiwa_ros2.git
 ```
Open new tweminal in ros2_ws
```
colcon build
```
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/ros2_ws/src/iiwa_ros2/iiwa_description/gazebo/models
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:~/ros2_ws/src/iiwa_ros2/iiwa_description/gazebo/models
ign gazebo ~/ros2_ws/src/iiwa_ros2/iiwa_description/gazebo/worlds/floating_marker.world

```
Open new terminal
```
ros2 run ros_gz_bridge parameter_bridge   /stereo_camera/right_link/right_rgb@sensor_msgs/msg/Image@gz.msgs.Image /stereo_camera/right_link/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo   --ros-args -r /stereo_camera/right_link/right_rgb:=/stereo/right/image_rect_color -r /stereo_camera/right_link/camera_info:=/stereo/right/camera_info
```
Open new terminal
```
ros2 launch aruco_ros single.launch.py eye:=right marker_id:=14 marker_size:=0.15

```
Open new terminal 
```
ros2 run rqt_image_view rqt_image_view

```
Select /aruco_single/result
