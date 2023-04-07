#!/usr/bin/env python3
import sys
import cv2
import rospy
import subprocess
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped
from cv_bridge import CvBridge, CvBridgeError


rtmp_url = "rtmp://52.66.197.49/live/ros"

command = ['ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "640x480",
       '-r', str(1),
        '-i', '-',
        '-c:v', 'libx264',
        '-b:v','2M',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        rtmp_url]

p = subprocess.Popen(command, stdin=subprocess.PIPE)

bridge = CvBridge()
def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(0)


def image_callback(img_msg):
    rospy.loginfo(img_msg.header)

    try:
        img = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    except CvBridgeError as e:
            print(e)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # gather video info to ffmpeg
    # width = img.shape[1]
    # height = img.shape[0]
    # print(width, height)
    p.stdin.write(img.tobytes())
    print("sent")

    # cv2.imshow("Image Window", img)
    cv2.waitKey(3)

def main():

    rospy.init_node('image_converter', anonymous=True)
    
    sub_image = rospy.Subscriber("/front_cam/camera/image", Image, image_callback)

    #cv2.namedWindow("Image Window", cv2.WINDOW_NORMAL)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down.")

    cv2.DestroyAllWindows()

if __name__ == '__main__':
    main()