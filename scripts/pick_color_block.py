#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019 RT Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
import moveit_commander
import actionlib
import math
#import random
from geometry_msgs.msg import Point, Pose
from gazebo_msgs.msg import ModelStates
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
from tf.transformations import quaternion_from_euler, euler_from_quaternion


from parameters import (
    GRIPPER_OPEN,
    GRIPPER_CLOSE,
    APPROACH_Z,
    LEAVE_Z,
    PICK_Z,
    PLACE_POSITIONS,
    BASE_POSITION
)



gazebo_model_states = ModelStates()

def callback(msg):
    global gazebo_model_states
    gazebo_model_states = msg


def yaw_of(object_orientation):
    # クォータニオンをオイラー角に変換しyaw角度を返す
    euler = euler_from_quaternion(
        (object_orientation.x, object_orientation.y,
        object_orientation.z, object_orientation.w))

    return euler[2]


def main():
    global gazebo_model_states

    
    i = 0
    flag = True

    sub_model_states = rospy.Subscriber("gazebo/model_states", ModelStates, callback, queue_size=1)

    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(0.4)
    arm.set_max_acceleration_scaling_factor(1.0)
    gripper = actionlib.SimpleActionClient("crane_x7/gripper_controller/gripper_cmd", GripperCommandAction)
    gripper.wait_for_server()
    gripper_goal = GripperCommandGoal()
    gripper_goal.command.max_effort = 2.0

    rospy.sleep(1.0)

    while True:
        flag = True
        # 何かを掴んでいた時のためにハンドを開く
        gripper_goal.command.position = 0.5
        gripper.send_goal(gripper_goal)
        gripper.wait_for_result(rospy.Duration(1.0))

        # SRDFに定義されている"home"の姿勢にする
        arm.set_named_target("home")
        arm.go()
        rospy.sleep(1.0)

        # 一定時間待機する
        # この間に、ユーザがgazebo上のオブジェクト姿勢を変更しても良い
        sleep_time = 1.0
        print("Wait " + str(sleep_time) + " secs.")
        rospy.sleep(sleep_time)
        print("Start")
        
        #if i < 18:
            #cube = OBJECT_NAME[i]

 
        # オブジェクトに接近する
        target_pose = Pose()
        place_position = PLACE_POSITIONS[i]
        target_pose.position.x = place_position.x
        target_pose.position.y = place_position.y
        target_pose.position.z = APPROACH_Z
        q = quaternion_from_euler(-math.pi, 0.0, -math.pi/2.0)
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to approach an object.")
            continue
        rospy.sleep(1.0)
        # 掴みに行く
        target_pose.position.z = PICK_Z
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to grip an object.")
            continue
        rospy.sleep(1.0)
        gripper_goal.command.position = GRIPPER_CLOSE
        gripper.send_goal(gripper_goal)
        gripper.wait_for_result(rospy.Duration(1.0))
        # 持ち上げる
        target_pose.position.z = LEAVE_Z
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to pick up an object.")
            continue
        rospy.sleep(1.0)

        # 一度、定めた座標を経由する
        place_position = BASE_POSITION
        target_pose.position.x = place_position.x
        target_pose.position.y = place_position.y
        #target_pose.position.z = APPROACH_Z
        q = quaternion_from_euler(-math.pi, 0.0, -math.pi/2.0)
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to approach base position.")
            continue
        rospy.sleep(1.0)
        
        # 設置位置に移動する
        place_position = PLACE_POSITIONS[i + 16] # 設置位置をランダムに選択する
        target_pose.position.x = place_position.x
        target_pose.position.y = place_position.y
        q = quaternion_from_euler(-math.pi, 0.0, -math.pi/2.0)
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to approach target position.")
            continue
        rospy.sleep(1.0)
        # 設置する
        target_pose.position.z = 0.11
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to place an object.")
            continue
        rospy.sleep(1.0)
        gripper_goal.command.position = GRIPPER_OPEN
        gripper.send_goal(gripper_goal)
        gripper.wait_for_result(rospy.Duration(1.0))
        # ハンドを上げる
        target_pose.position.z = LEAVE_Z
        arm.set_pose_target(target_pose)
        if arm.go() is False:
            flag = False
            print("Failed to leave from an object.")
            continue
        rospy.sleep(1.0)
        # SRDFに定義されている"home"の姿勢にする
        arm.set_named_target("home")
        if arm.go() is False:
            flag = False
            print("Failed to go back to home pose.")
            continue
        rospy.sleep(1.0)
        print("Done")
        if flag == True:
            i += 1
        print(i)
        if i > 15:
            print("Finish")
            break

if __name__ == '__main__':
    rospy.init_node("pick_and_place_in_gazebo_example")

    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
