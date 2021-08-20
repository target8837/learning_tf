#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import PositionTarget

import tf

#position_pub = rospy.Publisher("/local_position/pose", PoseStamped, queue_size = 1)
publisher = rospy.Publisher('mavros/setpoint_raw/local', PositionTarget, queue_size=3)

px = 0
py = 0

def mav_pos_cb(msg):
    global px, py
    px = msg.pose.position.x
    py = msg.pose.position.y
    pose = PositionTarget()
    pose.coordinate_frame = 1
    pose.position.x = px
    pose.position.y = py
    pose.position.z = 1
    pose.yaw = 0
    publisher.publish(pose)

def mav_pose():
    pose = PositionTarget()
    pose.coordinate_frame = 1
    pose.position.x = px
    pose.position.y = py
    pose.position.z = 1
    pose.yaw = 0
    publisher.publish(pose)


if __name__ == '__main__':
    rospy.init_node('mavros_tf_broadcaster')
    rospy.Subscriber('/local_position/pose',
                     PoseStamped,
                     mav_pos_cb,
                     queue_size = 1)
    mav_pose()
    rospy.spin()
