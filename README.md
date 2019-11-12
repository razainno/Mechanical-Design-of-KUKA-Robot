



## Quick Start to launch in gazebo 
1)  First open the Terminal and apply this command
        git clone https://github.com/razainno/kuka_robot_urdf.git
        cd kuka_robot_urdf/
        catkin_make
        source devel/setup.bash 
        roslaunch box_robot gazebo1.launch 

## launch of the controller to see the movement of the Robot
   open the terminal and apply these command 
        cd kuka_robot_urdf/
        catkin_make
        source devel/setup.bash
        cd src/rrbot_control/scripts/
        rosrun rrbot_control mains.py


## Robot display with Rviz 
![](kuka_robot.png.png)



## video link is given below


[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/IKFGcrc6w74/0.jpg)](http://www.youtube.com/watch?v=d_uQJWerai4)

