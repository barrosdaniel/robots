# Define the DriveBot class here!
class DriveBot:
    def __init__(self, motor_speed = 0, direction = 0, sensor_range = 0):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_range):
        self.sensor_range = new_range

robot_1 = DriveBot(5, 90, 10)
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)