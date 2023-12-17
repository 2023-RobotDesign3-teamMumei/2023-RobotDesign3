# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-FileCopyrightText: 2023 Shinnosuke Nonaka 
# SPDX-License-Identifier: Apache-2.0

# パラメータ定義用ファイル


from geometry_msgs.msg import Point

GRIPPER_OPEN = 0.30              # 掴む時のハンド開閉角度
GRIPPER_CLOSE = 0.17             # 設置時のハンド開閉角度
APPROACH_Z = 0.15                # 接近時のハンドの高さ
LEAVE_Z = 0.22                   # 離れる時のハンドの高さ
PICK_Z = 0.11                    # 掴む時のハンドの高さ
PLACE_POSITIONS = [             # オブジェクトの設置位置
            Point(0.3, -0.2, 0.0),
            Point(0.0, 0.3, 0.0),
            Point(0.0, -0.3, 0.0),
            Point(0.2, 0.2, 0.0),
            Point(0.2, -0.3, 0.0),
            Point(0.1, -0.4, 0.0),
            Point(0.4, 0.2, 0.0),
            Point(0.3, 0.3, 0.0),
            Point(0.3, -0.3, 0.0),
            Point(0.1, 0.2, 0.0),
            Point(0.1, -0.3, 0.0),
            Point(0.1, 0.3, 0.0),
            Point(0.0, 0.2, 0.0),
            Point(0.2, 0.3, 0.0),
            Point(0.3, 0.2, 0.0),
            Point(0.0, -0.2, 0.0),
            Point(0.42, -0.14, 0.0),
            Point(0.42, -0.07, 0.0),
            Point(0.42, 0.0, 0.0),
            Point(0.42, 0.07, 0.0),
            Point(0.35, -0.14, 0.0),
            Point(0.35, -0.07, 0.0),
            Point(0.35, 0.0, 0.0),
            Point(0.35, 0.07, 0.0),
            Point(0.28, -0.14, 0.0),
            Point(0.28, -0.07, 0.0),
            Point(0.28, 0.0, 0.0),
            Point(0.28, 0.07, 0.0),
            Point(0.21, -0.14, 0.0),
            Point(0.21, -0.07, 0.0),
            Point(0.21, 0.0, 0.0),
            Point(0.21, 0.07, 0.0)]
BASE_POSITION = Point(0.2, 0.0, 0.0)

#TP = Point(0.025,-0.375,0)#ターゲットポジション
PP = Point(PLACE_POSITIONS.x+0.1,PLACE_POSITIONS.y+0.1,0.45)#ターゲットポジションからx,y方向で0.1を足したもの
SMP = Point(PP.x+0.05,PP.y,0.11)#直接経路衝突回避のための経由地点
SP = Point(SMP.x,PP.y,0.11)#ストッパに向けてアームを動かすときのスタート地点x
YSX = Point(SMP.x-0.166,PP.y,0.11)#ブロックをx方向に向かって引きずるプログラム
SP2 = Point(PP.x-0.093,PP.y + 0.1,0.11)#ストッパに向けてアームを動かすときのスタート地点y
YSY = Point(SP2.x,SP2.y -0.18,0.1)#ブロックをy方向に向かって引きずるプログラム
