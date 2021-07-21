#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from geometry_msgs.msg import PoseStamped

import tf


def mav_pos_cb(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((0,0,0),
                     (msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w),
                     rospy.Time.now(),
                     "base_link",
                     "world")

if __name__ == '__main__':
    rospy.init_node('mavros_tf_broadcaster')
    rospy.Subscriber('/mavros/local_position/pose',
                     PoseStamped,
                     mav_pos_cb,
                     queue_size = 1)
    rospy.spin()
