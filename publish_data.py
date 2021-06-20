import rospy
from std_msgs.msg import Int32

pub = rospy.Publisher('/test', Int32, queue_size=10)
rospy.init_node('publisher1')
r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
   pub.publish(1)
   r.sleep()
