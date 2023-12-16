# Define the DriveBot class here!
class DriveBot:
    def __init__(self, motor_speed = 0, direction = 0, sensor_range = 0):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

robot_1 = DriveBot(5, 90, 10)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)