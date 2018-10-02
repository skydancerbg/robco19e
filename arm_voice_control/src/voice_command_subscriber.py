#!/usr/bin/env python
import rospy
import roslaunch
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Voice comman received:  %s", data.data)

# import roslaunch
# package = 'PACKACKE_NAME'
# executable = 'YOUR_SCRIPT.py'
# node_name = 'YOUR_NODE_NAME'
# node = roslaunch.core.Node(package=package, node_type=executable, name=node_name)
# launch = roslaunch.scriptapi.ROSLaunch()
# launch.start() 
# process = launch.launch(node)

    package = 'mover4_moveit_config'
    executable = 'mover4_named_position_replay.py'
    node_name = 'mover4_move_group_python_interface'
    node = roslaunch.core.Node(package=package, node_type=executable, name=node_name)
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start() 
    process = launch.launch(node)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('arm_voice_command_listener', anonymous=True)

    rospy.Subscriber("arm_control/voice_command", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()