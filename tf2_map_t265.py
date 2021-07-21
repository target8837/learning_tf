#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from nav_msgs.msg import Odometry

import tf


def handle_camera_pose(msg, cameraname):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z),
                     (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w),
                     rospy.Time.now(),
                     "t265_odom_frame",
                     "world")

if __name__ == '__main__':
    rospy.init_node('camera_tf_broadcaster')
    cameraname = rospy.get_param('~camera')
    framename = rospy.get_param('~frame')
    rospy.Subscriber('/%s/odom/sample' % cameraname,
                     Odometry,
                     handle_camera_pose,
                     cameraname)
    rospy.spin()
