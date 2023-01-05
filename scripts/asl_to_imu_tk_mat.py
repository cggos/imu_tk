import sys
sys.path.append("../../imu_benchmark")

import imu_data

if __name__ == "__main__":
    data_dir = "./data/"
    read_imu = imu_data.ReadIMU(data_dir)

    imu_d435i = read_imu.from_ts_gyr_acc("imu_tk.csv")

    gyr_path = data_dir + "gyr.mat"
    acc_path = data_dir + "acc.mat"

    of_gyr = open(gyr_path, 'w')
    of_acc = open(acc_path, 'w')

    for i in range(len(imu_d435i)):
        imu = imu_d435i[i]  # type:imu_data.IMU
        of_gyr.write("{} {} {} {}\n".format(imu.timestamp, imu.gyr.x, imu.gyr.y, imu.gyr.z))
        of_acc.write("{} {} {} {}\n".format(imu.timestamp, imu.acc.x, imu.acc.y, imu.acc.z))

    of_gyr.close()
    of_acc.close()


