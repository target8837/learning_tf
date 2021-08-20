#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Image

import tf

position_pub = rospy.Publisher("/local_position/pose", PoseStamped, queue_size = 1)
depth_pub = rospy.Publisher("/depth_image", Image, queue_size = 1)

depth_stamp = 0

def mav_pos_cb(msg):
    pose = PoseStamped()
    pose.header.seq = 1
    pose.header.stamp = msg.header.stamp
    pose.header.frame_id = "map"

    pose.pose.position.x = msg.pose.position.y
    pose.pose.position.y = msg.pose.position.x
    pose.pose.position.z = msg.pose.position.z

    pose.pose.orientation.x = msg.pose.orientation.x
    pose.pose.orientation.y = msg.pose.orientation.y
    pose.pose.orientation.z = msg.pose.orientation.z
    pose.pose.orientation.w = msg.pose.orientation.w

    position_pub.publish(pose)

def depth_cb(msg):
    #global depth_stamp
    #depth_stamp = msg.header.stamp
    img = Image()
    img.header.seq = 1
    img.header.frame_id = "map"
    img.header.stamp = rospy.Time.now()

    img.height = msg.height
    img.width = msg.width

    img.encoding = msg.encoding

    img.is_bigendian = msg.is_bigendian
    img.step = msg.step
    img.data = msg.data
    depth_pub.publish(img)

if __name__ == '__main__':
    rospy.init_node('mavros_tf_broadcaster')
    rospy.Subscriber('/mavros/local_position/pose',
                     PoseStamped,
                     mav_pos_cb,
                     queue_size = 1)
    rospy.Subscriber('/depth_camera',
                     Image,
                     depth_cb,
                     queue_size = 1)
    rospy.spin()
