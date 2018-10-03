#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
# rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
rospy.init_node('mover4_move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("robot")
gripper = moveit_commander.MoveGroupCommander("gripper")
# display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

# create publisher to send reset connect motor enable commands
# mover4_hardware_commands_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)


rospy.loginfo("NACHALOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

# pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 1.0
# pose_target.position.x = 0.96
# pose_target.position.y = 0
# pose_target.position.z = 1.18
# group.set_pose_target(pose_target)  GripperOpen GripperClose

gripper.set_named_target("GripperOpen")
# planG1 = gripper.plan()
# rospy.sleep(5)
# gripper.go(wait=True)

# plan = gripper.go(wait=True)
# gripper.stop()

planL = gripper.plan()
gripper.execute(planL)
gripper.clear_pose_targets()
rospy.loginfo("OTVORIIIIIIIIIIIIIIIIII")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


gripper.set_named_target("GripperClose")
# planG1 = gripper.plan()
# rospy.sleep(5)
# gripper.go(wait=True)

# plan1 = gripper.go(wait=True)
# gripper.stop()

plan1 = gripper.plan()
gripper.execute(plan1)

gripper.clear_pose_targets()
rospy.loginfo("ZATVORIIIIIIIIIIIIIIIIII")

# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# group.set_named_target("transport_position")
# plan1 = group.plan()
# # rospy.sleep(5)
# group.go(wait=True)

group.set_named_target("reach_up")
# plan2 = group.plan()
# rospy.sleep(5)
# group.go(wait=True)
# plan2 = group.go(wait=True)
# # Calling `stop()` ensures that there is no residual movement
# group.stop()
# # It is always good to clear your targets after planning with poses.
# # Note: there is no equivalent function for clear_joint_value_targets()
# group.clear_pose_targets()
# rospy.sleep(10)

plan2 = group.plan()
group.execute(plan2)
gripper.clear_pose_targets()
rospy.loginfo("reach_up")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


group.set_named_target("place_on_tall_table")
# plan2 = group.plan()
# rospy.sleep(5)
# group.go(wait=True)
# # plan3 = group.go(wait=True)
# # group.stop()
# # group.clear_pose_targets()
# # rospy.sleep(10)
plan3 = group.plan()
group.execute(plan3)
gripper.clear_pose_targets()
rospy.loginfo("place_on_tall_table")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


gripper.set_named_target("GripperOpen")
# planG1 = gripper.plan()
# rospy.sleep(5)
# gripper.go(wait=True)
# plan4 = group.go(wait=True)
# gripper.stop()
# gripper.clear_pose_targets()
# rospy.sleep(10)
plan4 = gripper.plan()
gripper.execute(plan4)
gripper.clear_pose_targets()
rospy.loginfo("OTVORIIIIIIIIIIIIIIIIII")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


group.set_named_target("release_bottle_on_tall_table")
# plan2 = group.plan()
# rospy.sleep(10)
# group.go(wait=True)
# # plan5 = group.go(wait=True)
# # group.stop()
# # group.clear_pose_targets()
# # rospy.sleep(10)
# # group.set_named_target("clear_of_tall_table")
plan5 = group.plan()
group.execute(plan5)
gripper.clear_pose_targets()
rospy.loginfo("release_bottle_on_tall_table")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# # plan6 = group.go(wait=True)
# # group.stop()
# # group.clear_pose_targets()
# # rospy.sleep(10)

group.set_named_target("transport_position")
# plan2 = group.plan()
# rospy.sleep(5)
# group.go(wait=True)
# # plan7 = group.go(wait=True)
# # group.stop()
# # group.clear_pose_targets()
# # rospy.sleep(10)
plan7 = group.plan()
group.execute(plan7)
gripper.clear_pose_targets()
rospy.loginfo("transport_position")
# rospy.sleep(10)
rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# # gripper.set_named_target("GripperClose")
# # # planG1 = gripper.plan()
# # # rospy.sleep(5)
# # # gripper.go(wait=True)
# # plan8 = gripper.go(wait=True)
# # gripper.stop()
# # gripper.clear_pose_targets()


# gripper.set_named_target("GripperOpen")
# gripper.go(wait=True)
# rospy.sleep(5)
# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)

moveit_commander.roscpp_shutdown()