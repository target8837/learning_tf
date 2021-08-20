#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from sensor_msgs.msg import Image

import tf


def depth_cb(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((0,0,0),
                     (0.0, 0.0, 0.0, 1.0),
                     rospy.Time.now(),
                     "/drone/X3/base_link/depth_camera1",
                     "map")

if __name__ == '__main__':
    rospy.init_node('mavros_depth_broadcaster')
    rospy.Subscriber('/depth_camera',
                     Image,
                     depth_cb,
                     queue_size = 1)
    rospy.spin()
