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

* 株式会社アールティ様から配布されている [crane_x7_ros](https://github.com/rt-net/crane_x7_ros) パッケージをインストール

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

作成したROSワークスペースにクローンしてください

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/2023-RobotDesign3-teamMumei/2023-RobotDesign3.git
$ ( cd ~/catkin_ws/ && catkin_make )
$ source ~/.bashrc
```

## 本パッケージの使用方法
* シミュレーションを使用する場合

GAZEBO上でCRANE_X7を用いた、実機の動作確認用のシミュレーション環境を起動します

このシミュレーションでは、RealSenseを使用することはできません

```
$ roslaunch 2023-RobotDesign3 crane_x7_with_table.launch
$ rosurun 2023-RobotDesign3 pick_color_block_in_gazebo.py
```

* 実機を使用する場合

CRANE_X7をPCに接続した状態で、デバイスファイルへの読み書きの実行権限を付与する

```
$ sudo chmod 666 /dev/ttyUSB0
```
実機の起動

コマンドを実行するとアームが動き出すので、周囲に注意して起動してください

```
$ 
$ 
```

---

## ライセンス
このソフトウェアパッケージは、株式会社アールティ様が提供するCRANE_X7の[LICENCE](https://github.com/rt-net/crane_x7_ros/blob/master/LICENSE)に基づいて作成しています。