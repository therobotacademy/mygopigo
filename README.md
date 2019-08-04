This repository is the evolution of [gopigo3_node](https://github.com/ros-gopigo/gopigo3_node) for using easy libraries of GoPiGo3 and DI sensors within a ROS enviroment (from Python scripts)

# Distance sensor
Run nodes manually:
```bash
T1 $ roscore
T2 $ rosrun mygopigo easyDistance.py
T3 $ rostopic echo /distance_sensor/distance
```
Using roslaunch:
```bash
T2 $ roslaunch mygopigo easyDistance.launch
T3 $ rostopic echo /distance_sensor/distance
```


