#!/usr/bin/env python3
# week2_exercise2 

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class Subscriber():

    def callback(self, odom_data):
        linear_x = odom_data.pose.pose.position.x
        linear_y = odom_data.pose.pose.position.y
        ori_x = odom_data.pose.pose.orientation.x
        ori_y = odom_data.pose.pose.orientation.y
        ori_z = odom_data.pose.pose.orientation.z
        ori_w = odom_data.pose.pose.orientation.w
        (roll, pitch, yaw) = euler_from_quaternion([ori_x, 
                     ori_y, ori_z, ori_w], 
                     'sxyz')
        print(f"position_x = '{linear_x}', position_y = '{linear_y}', position_thetaz = '{yaw}'")
        #print(f"The '{self.node_name}' node obtained the following message: '{topic_message.data}'")

    def __init__(self):
        self.node_name = "odom_subscriber"
        topic_name = "/odom"

        rospy.init_node(self.node_name, anonymous=True)
        self.sub = rospy.Subscriber(topic_name, Odometry, self.callback)
        rospy.loginfo(f"The '{self.node_name}' node is active...")

    def main_loop(self):
        rospy.spin()

if __name__ == '__main__':
    subscriber_instance = Subscriber()
    subscriber_instance.main_loop()
