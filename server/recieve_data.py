import rospy
#from rospy_tutorials.msg import HeaderString
from geometry_msgs.msg import Twist
import subprocess
import std_msgs

def callback(data):
    now = rospy.get_rostime()
    str_data =  data.data
    time = data.header.stamp
    convert_to_sec = (float(str(now)) - float(str(time)))*(10**-9)
    convert_to_hz = 1 / convert_to_sec
    rospy.loginfo("Sent at %s Current time: %s \t diff %s", time, now, convert_to_sec)

def turtle_callback(data):
    print(data)
    print(data.header.stamp)
    
def listener():
    rospy.init_node('test_2')
#    rospy.Subscriber("/test", HeaderString, callback)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, turtle_callback)    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

listener()
