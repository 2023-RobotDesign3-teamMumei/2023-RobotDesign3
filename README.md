# RobotDesign3_2023

本パッケージは、ロボット設計製作論実習３知能コースの講義内で無名班が作成した、ドット文字を作るROSパッケージです。このパッケージは、[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)を元に制作したものです。

## 動作確認済み環境
  * OS: Ubuntu 20.04LTS
  * ROS: Noetic
  * Intel RealSense SDK 2.0
  * OpenCV 4.5.1

## セットアップ方法

* ROSのインストール
```
$ git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop.git
$ cd ros_setup_scripts_Ubuntu18.04_desktop/
$ sudo apt update
$ sudo apt upgrade
$ ./locale.ja.bash
$ ./step0.bash
$ ./step1.bash
```
* ROSの動作確認
```
$ source ~/.bashrc
$ roscore
```
* ワークスペースの作成
```
$ cd
$ mkdir -p catkin_ws/src
$ cd catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ vi ~/.bashrc  #~/.bashrcの編集
・・・
source /opt/ros/melodic/setup.bash        #追加
source ~/catkin_ws/devel/setup.bash       #追加
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
・・・
$ source ~/.bashrc
$ cd ~/catkin_ws/
$ catkin_make
```

* 株式会社アールティ様から配布されている crane_x7_ros パッケージをインストール
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/rt-net/crane_x7_ros.git
$ git clone https://github.com/rt-net/crane_x7_description.git
$ git clone https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins.git
$ rosdep install -r -y --from-paths --ignore-src crane_x7_ros
$ ( cd ~/catkin_ws/ && catkin_make )
```

* Rvizの動作確認
```
$ source ~/.bashrc
$ roscore &
$ rviz
```
* GAZEBOの動作確認

~/.ignition/fuel/config.yamlを編集する
```
$ cd ~/.ignition/fuel/
$ vi config.yaml
・・・
servers:    #この行以下を追加
-
  name: osrf
  url: https://api.ignitionrobotics.org
・・・
```
GAZEBOを起動
```
$ roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

* RealSense

* OpenCVのインストール
```
$ wget --no-check-certificate https://raw.githubusercontent.com/milq/milq/master/scripts/bash/install-opencv.sh
$ chmod +x install-opencv.sh
$ ./install-opencv.sh
```
* 本パッケージのインストール
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/2023-RobotDesign3-teamMumei/2023-RobotDesign3.git
```

## 本パッケージの使用方法

---

## ライセンス