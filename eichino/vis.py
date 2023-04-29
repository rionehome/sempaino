#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

class Vis():
    def __init__(self):
        rospy.init_node("vis")
        self.sub = rospy.Subscriber("/mobile_base/commands/velocity", Twist, self.value_print)
        self.linear = 0
        self.angular = 0
        self.main()
    
    def value_print(self, message):
        self.linear = message.linear.x
        self.angular = message.angular.z
    
    def main(self):
        start_time = time.time()
        while not rospy.is_shutdown():
            print("ela_time: " + str(round(time.time() - start_time, 5)) + "\n" \
                + "linear  : " + str(self.linear) + "\n" \
                + "angular : " + str(self.angular) + "\n" + "\033[3A", end="")
            rospy.Rate(10).sleep()

if __name__=='__main__':
    vis = Vis()