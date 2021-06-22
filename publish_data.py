import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/test', String, queue_size=10)
rospy.init_node('publisher1')
r = rospy.Rate(30) # 10hz
while not rospy.is_shutdown():
   time = str(rospy.get_rostime().secs) + "." + str(rospy.get_rostime().nsecs)
   pub.publish(time)
   r.sleep()
