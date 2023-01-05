import numpy as np

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu

acc_misalignment = np.array([[1, 0.0194692, -0.0574956], [0, 1, -0.00366816], [0,0,1]])
acc_scale = np.diag([1.00773, 1.01848, 1.01499])
acc_bias = np.array([-0.19119, 0.57394, -0.231325]).reshape(3,1)

print("acc_misalignment: \n {}".format(acc_misalignment))
print("acc_scale: \n {}".format(acc_scale))
print("acc_bias: \n {}".format(acc_bias))

data_dir = "./data/"
acc_norm = data_dir + "acc_norm.txt"
of_acc_norm = open(acc_norm,'w')

def callback(data): # data: Imu
  gyr_data = np.array([data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z]).reshape(3,1)
  acc_data = np.array([data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z]).reshape(3,1)

  # acc correction
  acc_correct = acc_misalignment.dot(acc_scale.dot(acc_data-acc_bias))

  acc_norm_raw = np.linalg.norm(acc_data)
  acc_norm_correct = np.linalg.norm(acc_correct)

  rospy.loginfo(" raw acc: {}, norm: {}".format(acc_data.reshape(3), acc_norm_raw))
  rospy.loginfo(" correct acc: {}, norm: {}".format(acc_correct.reshape(3), acc_norm_correct))

  of_acc_norm.write("{},{}\n".format(acc_norm_raw, acc_norm_correct))


def imu_listener():
    pub = rospy.Publisher('/imu_correction', Imu, queue_size=10)
    rospy.init_node('imu_listener', anonymous=True)
    rospy.Subscriber("/camera/imu", Imu, callback)
    rospy.spin()

def main(_):
  try:
    rospy.loginfo("start IMU correction")
    imu_listener()
  except rospy.ROSInterruptException:
    of_acc_norm.close()
    pass

if __name__ == "__main__":
  main('_')

    
