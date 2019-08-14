#!/usr/bin/env python

# BEGIN ALL
import rospy
from sensor_msgs.msg import Range
# from std_msgs.msg import Int32


# BEGIN CALLBACK
def callback(msg):
    print msg.data
    rospy.loginfo(rospy.get_caller_id() + 'GoPiGo3 measures distance %s mm', msg.data*1000)
# END CALLBACK


rospy.init_node('distance_sensor_subscriber')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('distance_sensor/distance', Range, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
