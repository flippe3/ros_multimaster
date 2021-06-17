import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo("I heard %d",data.data)
    
def listener():
    rospy.init_node('test')
    rospy.Subscriber("/test", Int32, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

listener()
