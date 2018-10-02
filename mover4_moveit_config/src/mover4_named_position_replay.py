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


# pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 1.0
# pose_target.position.x = 0.96
# pose_target.position.y = 0
# pose_target.position.z = 1.18
# group.set_pose_target(pose_target)

# gripper.set_named_target("GripperClose")
# planG1 = gripper.plan()
# rospy.sleep(2)
# gripper.go(wait=True)

# # group.set_named_target("transport_position")
# # plan1 = group.plan()
# # # rospy.sleep(5)
# # group.go(wait=True)

group.set_named_target("reach_up")
plan2 = group.plan()
rospy.sleep(15)
group.go(wait=True)

group.set_named_target("place_on_tall_table")
plan2 = group.plan()
rospy.sleep(15)
group.go(wait=True)

# gripper.set_named_target("GripperOpen")
# planG1 = gripper.plan()
# rospy.sleep(5)
# gripper.go(wait=True)

group.set_named_target("release_bottle_on_tall_table")
plan2 = group.plan()
rospy.sleep(15)
group.go(wait=True)

group.set_named_target("clear_of_tall_table")
plan2 = group.plan()
rospy.sleep(15)
group.go(wait=True)

group.set_named_target("transport_position")
plan2 = group.plan()
rospy.sleep(15)
group.go(wait=True)

# gripper.set_named_target("GripperOpen")
# gripper.go(wait=True)
# rospy.sleep(5)
# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)

moveit_commander.roscpp_shutdown()