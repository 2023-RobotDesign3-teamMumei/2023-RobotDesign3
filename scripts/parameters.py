# parameters.py

from geometry_msgs.msg import Point

GRIPPER_OPEN = 0.30              # 掴む時のハンド開閉角度
GRIPPER_CLOSE = 0.17             # 設置時のハンド開閉角度
APPROACH_Z = 0.15                # 接近時のハンドの高さ
LEAVE_Z = 0.22                   # 離れる時のハンドの高さ
PICK_Z = 0.12                    # 掴む時のハンドの高さ
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
            Point(0.42, -0.07, 0.0), # 7mm間隔にする
            Point(0.42, 0.0, 0.0),
            Point(0.42, 0.07, 0.0),
            Point(0.35, -0.07, 0.0),
            Point(0.35, 0.0, 0.0),
            Point(0.35, 0.07, 0.0),
            Point(0.28, -0.07, 0.0),
            Point(0.28, 0.0, 0.0),
            Point(0.28, 0.07, 0.0)]
BASE_POSITION = Point(0.2, 0.0, 0.0)

ALPHA_POS_A = []
