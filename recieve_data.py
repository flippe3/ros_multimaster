import rospy
from std_msgs.msg import String
import subprocess
import std_msgs

def get_time_difference():
    # Gets the local time from each machine with a ROS call
    data = subprocess.check_output("rosservice call /master_discovery/list_masters | grep -iw 'name:\|timestamp_local'", shell=True).replace("\"", "").split("\n")

    # Removes whitespaces and other stuff to only get the actual time.
    print(data)
    data_clean = []
    for i in data[:-1]:
        data_clean.append((i.split(": ")[1]))
    print(data_clean)

    times = []
    names = []
    for i in range(0, len(data_clean)):
        if i % 2 == 0:
            names.append(data_clean[i])
        else:
            times.append(float(data_clean[i]))
    print(names, times)
    # Calculate the difference from host (the first time is the host)
    time_diff = []
    for i in times:
        time_diff.append(times[0] - i)
    print(time_diff)
    return time_diff

def callback(data):
    current_time = str(rospy.get_rostime().secs) + "." + str(rospy.get_rostime().nsecs)
    rospy.loginfo("I heard %s current_time: %d", data.data, float(str(current_time)) - float(data.data))
    #rospy.loginfo("I heard %s", data.machine)
    
def listener():
    rospy.init_node('test_2')
    rospy.Subscriber("/test", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

#diff = get_time_difference()
listener()
