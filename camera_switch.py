#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo

import tf

color_pub = rospy.Publisher("/color_image", Image, queue_size = 10)
depth_pub = rospy.Publisher("/depth_image", Image, queue_size = 10)
info_pub = rospy.Publisher("/image_info", CameraInfo, queue_size = 10)

def depth_cb(msg):
    #global depth_stamp
    #depth_stamp = msg.header.stamp
    img = Image()
    img.header.seq = msg.header.seq
    img.header.frame_id = msg.header.frame_id
    img.header.stamp = rospy.Time.now()

    img.height = msg.height
    img.width = msg.width

    img.encoding = msg.encoding

    img.is_bigendian = msg.is_bigendian
    img.step = msg.step
    img.data = msg.data
    depth_pub.publish(img)

def color_cb(msg):
    #global depth_stamp
    #depth_stamp = msg.header.stamp
    img = Image()
    img.header.seq = msg.header.seq
    img.header.frame_id = msg.header.frame_id
    img.header.stamp = rospy.Time.now()

    img.height = msg.height
    img.width = msg.width

    img.encoding = msg.encoding

    img.is_bigendian = msg.is_bigendian
    img.step = msg.step
    img.data = msg.data
    color_pub.publish(img)

def ci_cb(msg):
    #global depth_stamp
    #depth_stamp = msg.header.stamp
    info = CameraInfo()
    info.header.seq = msg.header.seq
    info.header.frame_id = msg.header.frame_id
    info.header.stamp = rospy.Time.now()

    info.height = msg.height
    info.width = msg.width

    info.distortion_model = msg.distortion_model
    info.D = msg.D
    info.K = msg.K
    info.R = msg.R
    info.P = msg.P

    info.binning_x = msg.binning_x
    info.binning_y = msg.binning_y
    
    info.roi = msg.roi
    info_pub.publish(info)

if __name__ == '__main__':
    rospy.init_node('mavros_depth_broadcaster')
    rospy.Subscriber('/d435/depth/image_rect_raw',
                     Image,
                     depth_cb,
                     queue_size = 1)
    rospy.Subscriber('/d435/color/image_raw',
                     Image,
                     color_cb,
                     queue_size = 1)
    rospy.Subscriber('/d435/color/camera_info',
                     CameraInfo,
                     ci_cb,
                     queue_size = 1)
    rospy.spin()
