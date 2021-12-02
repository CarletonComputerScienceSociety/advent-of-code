# Thomas Selwyn
# 01-Dec-2021

sonar_depth_data = []

# Read Sonar Sensor (data/day_1.txt)
with open('data/day_1.txt') as sonar_depth_sensor:
    sonar_depth_sensor_readings = sonar_depth_sensor.readlines()
    sonar_depth_sensor.close()

    for sensor_reading in sonar_depth_sensor_readings:
        sonar_depth_data.append(int(sensor_reading.strip()))

print(sonar_depth_data)

# PART ONE
# Count how many times the measurement is larger
sonar_depth_increases = 0

for i in range(1, len(sonar_depth_data)):
    if sonar_depth_data[i] > sonar_depth_data[i - 1]:
        sonar_depth_increases += 1

print("The measurement has been larger than the previous measurement, {} times!".format(sonar_depth_increases))

# PART TWO
# Count how many times the three-measurement sliding window is larger
sonar_data_sliding_sum = []
sonar_depth_sum_increases = 0

for i in range(len(sonar_depth_data) - 2):
    sonar_data_sliding_sum.append(sum(sonar_depth_data[i:i+3]))

    if sonar_data_sliding_sum[i] > sonar_data_sliding_sum[i - 1]:
        sonar_depth_sum_increases += 1

print("The sliding sum has been larger than the previous sliding sum, {} times!".format(sonar_depth_sum_increases))