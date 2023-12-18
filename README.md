# RobotDesign3_2023

本パッケージは、ロボット設計製作論実習３知能コースの講義内で無名班が作成した、ドット文字を作るROSパッケージです。このパッケージは、[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)を元に制作したものです。

## 動作確認済み環境
  * OS: Ubuntu 20.04LTS
  * ROS: Noetic
  * Rviz 1.14.20
  * GAZEBO 11.11.0

## セットアップ方法

* ROSパッケージをインストールし、ワークスペースを作成します

* 株式会社アールティ様から配布されている [crane_x7_ros](https://github.com/rt-net/crane_x7_ros) パッケージを、作成したワークスペースにインストールします

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/rt-net/crane_x7_ros.git
$ git clone https://github.com/rt-net/crane_x7_description.git
$ git clone https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins.git
$ rosdep install -r -y --from-paths --ignore-src crane_x7_ros
$ ( cd ~/catkin_ws/ && catkin_make )
```

GAZEBOを起動して動作を確認します

```
$ roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

* 本パッケージのインストール

作成したROSワークスペースに`git clone`でインストールしてください

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/2023-RobotDesign3-teamMumei/2023-RobotDesign3.git
$ ( cd ~/catkin_ws/ && catkin_make )
$ source ~/.bashrc
```

## 本パッケージの使用方法
* シミュレーションを使用する場合

GAZEBO上でCRANE_X7を用いた、実機の動作確認用のシミュレーション環境を起動します

```
$ roslaunch 2023-RobotDesign3 crane_x7_with_table.launch
$ rosurun 2023-RobotDesign3 pick_color_block_in_gazebo.py
```

* 実機を使用する場合

以下のようにブロックとストッパーを配置してください

![image](C:\Users\81807\Pictures\Screenshots\スクリーンショット 2023-12-18 101514.png)

CRANE_X7をPCに接続した状態で、デバイスファイルへの読み書きの実行権限を付与する

```
$ sudo chmod 666 /dev/ttyUSB0
```
実機の起動

コマンドを実行するとアームが動き出すので、周囲に注意して起動してください

```
$ roslaunch crane_x7_bringup demo.launch fake_execution:=false
$ rosrun 2023-RobotDesign3 pick_color_block.py
```

---

## ライセンス
このソフトウェアパッケージは、株式会社アールティ様が提供するCRANE_X7の[LICENCE](https://github.com/rt-net/crane_x7_ros/blob/master/LICENSE)に基づいて作成しています。
