import rospy
from std_msgs.msg import String
from rospy_tutorials.msg import HeaderString

pub = rospy.Publisher('/test', String, queue_size=10)
rospy.init_node('publisher1')
r = rospy.Rate(30) # 10hz

while not rospy.is_shutdown():
   now = rospy.get_rostime()
   time = str(now.secs) + "." + str(now.nsecs)
   pub.publish(time)
   r.sleep()
