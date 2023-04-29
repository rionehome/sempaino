#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.5
TIME = 1.0

class ittan():
    def __init__(self, linear=LINEAR_SPEED, angular=ANGULAR_SPEED, time=TIME):
        rospy.init_node("ittan")
        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=1)
        self.t = Twist()
        self.linear = linear
        self.angular = angular
        self.time = time
    
    def forword(self):
        self.t.linear.x = self.linear
        self.t.angular.z = 0
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time < self.time:
            self.pub.publish(self.t)
            end_time = time.time()
        time.sleep(0.5)
    
    def back(self):
        self.t.linear.x = -self.linear
        self.t.angular.z = 0
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time < self.time:
            self.pub.publish(self.t)
            end_time = time.time()
        time.sleep(0.5)
    
    def left(self):
        self.t.linear.x = 0
        self.t.angular.z = self.angular
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time < self.time:
            self.pub.publish(self.t)
            end_time = time.time()
        time.sleep(0.5)
        
    def right(self):
        self.t.linear.x = 0
        self.t.angular.z = -self.angular
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time < self.time:
            self.pub.publish(self.t)
            end_time = time.time()
        time.sleep(0.5)
    
    def custom(self):
        self.t.linear.x = self.linear
        self.t.angular.z = self.angular
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time < self.time:
            self.pub.publish(self.t)
            end_time = time.time()
        time.sleep(0.5)