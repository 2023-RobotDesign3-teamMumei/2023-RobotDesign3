# RobotDesign3_2023

本パッケージは、ロボット設計製作論実習３知能コースの講義内で無名班が、作成したドット文字を作るROSパッケージです。このパッケージは、[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)を元に制作したものです。

# セットアップ方法

* 本パッケージのインストール
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/2023-RobotDesign3-teamMumei/2023-RobotDesign3.git
```

* 株式会社アールティ様から配布されている crane_x7_ros をダウンロード
```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/crane_x7_ros.git
```

* OpenCVのインストール
```
$ wget --no-check-certificate https://raw.githubusercontent.com/milq/milq/master/scripts/bash/install-opencv.sh
$ chmod +x install-opencv.sh
$ ./install-opencv.sh
```

## 動作確認済み環境
  * OS: Ubuntu 20.04LTS
  * ROS: Noetic
  * Intel RealSense SDK 2.0
  * OpenCV 4.5.1

---
