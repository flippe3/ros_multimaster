import rospy
from std_msgs.msg import String
import subprocess
import std_msgs

def callback(data):
    now = rospy.get_rostime()
    now_str = str(now.secs) + "." + str(now.nsecs)
    rospy.loginfo("Sent at %s Current time: %s \t difference: %s", data.data, now_str, str(float(now_str) - float(data.data)))
    #rospy.loginfo("I heard %s", data.machine)
    
def listener():
    rospy.init_node('test_2')
    rospy.Subscriber("/test", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

#diff = get_time_difference()
listener()
