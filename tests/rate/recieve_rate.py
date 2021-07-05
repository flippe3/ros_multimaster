import rospy
from rospy_tutorials.msg import HeaderString
from std_msgs.msg import Int16

msg_count = 0 

def callback(data):
    global msg_count
    if data.data == 0:
        msg_count += 1
    else:
        print("Messages recieved: ", msg_count, " messages sent: ", data.data, " missed msgs: ", data.data - msg_count, " over one second.")
        msg_count = 0 
    
def header_listener():
    rospy.init_node('test_2')
    rospy.Subscriber("/test", HeaderString, callback)
    rospy.spin()
    
def int_listener():
    rospy.init_node('test_2')
    rospy.Subscriber("/test", Int16, callback)
    rospy.spin()

int_listener()
