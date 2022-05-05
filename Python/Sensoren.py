import smbus # system management bus
import math

GRAVITIY_MS2 = 9.80665

# Scale Modifiers
ACCEL_SCALE_MODIFIER_2G = 16384.0
ACCEL_SCALE_MODIFIER_4G = 8192.0
ACCEL_SCALE_MODIFIER_8G = 4096.0
ACCEL_SCALE_MODIFIER_16G = 2048.0

GYRO_SCALE_MODIFIER_250DEG = 131.0
GYRO_SCALE_MODIFIER_500DEG = 65.5
GYRO_SCALE_MODIFIER_1000DEG = 32.8
GYRO_SCALE_MODIFIER_2000DEG = 16.4

# Pre-defined ranges
ACCEL_RANGE_2G = 0x00
ACCEL_RANGE_4G = 0x08
ACCEL_RANGE_8G = 0x10
ACCEL_RANGE_16G = 0x18

GYRO_RANGE_250DEG = 0x00
GYRO_RANGE_500DEG = 0x08
GYRO_RANGE_1000DEG = 0x10
GYRO_RANGE_2000DEG = 0x18

FILTER_BW_256=0x00
FILTER_BW_188=0x01
FILTER_BW_98=0x02
FILTER_BW_42=0x03
FILTER_BW_20=0x04
FILTER_BW_10=0x05
FILTER_BW_5=0x06

# MPU-6050 Registers
PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C

ACCEL_XOUT0 = 0x3B
ACCEL_YOUT0 = 0x3D
ACCEL_ZOUT0 = 0x3F

TEMP_OUT0 = 0x41

GYRO_XOUT0 = 0x43
GYRO_YOUT0 = 0x45
GYRO_ZOUT0 = 0x47

ACCEL_CONFIG = 0x1C
GYRO_CONFIG = 0x1B
MPU_CONFIG = 0x1A

class Sensor:
    def __init__(self, bus_num, address):
        self.bus = smbus.SMBus(bus_num) # set bus
        self.address = address # set address
        self.bus.write_byte_data(address, PWR_MGMT_1, FILTER_BW_256) # activate
    
    def set_accel_range(self, accel_range):
        self.bus.write_byte_data(self.address, ACCEL_CONFIG, 0x00)
        self.bus.write_byte_data(self.address, ACCEL_CONFIG, accel_range)

    def set_gyro_range(self, gyro_range):
        self.bus.write_byte_data(self.address, GYRO_CONFIG, 0x00)
        self.bus.write_byte_data(self.address, GYRO_CONFIG, gyro_range)

    def set_filter_range(self, filter_range=FILTER_BW_256):
        #Sets the low-pass bandpass filter frequency
        # Keep the current EXT_SYNC_SET configuration in bits 3, 4, 5 in the MPU_CONFIG register
        EXT_SYNC_SET = self.bus.read_byte_data(self.address, MPU_CONFIG) & 0b00111000
        return self.bus.write_byte_data(self.address, MPU_CONFIG,  EXT_SYNC_SET | filter_range)

    def read_byte(self, reg):
        return self.bus.read_byte_data(self.address, reg)
 
    def read_word(self, reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        value = (h << 8) + l
        return value
 
    def read_word_2c(self, reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
 
    def dist(self, a,b):
        return math.sqrt((a*a)+(b*b))
    
    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)
    
    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)    

    def get_temp(self):
        raw_temp = self.read_i2c_word(TEMP_OUT0)
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp

    def getAccData(self):
        acceleration_data = {
            "xAxis": self.read_word_2c(ACCEL_XOUT0),# / self.accel_scale_mod,
            "yAxis": self.read_word_2c(ACCEL_YOUT0),# / self.accel_scale_mod,
            "zAxis": self.read_word_2c(ACCEL_ZOUT0)# / self.accel_scale_mod
        }
        return acceleration_data

    def getGyrData(self):
        gyroscope_data = {
            "xAxis": self.read_word_2c(0x43),
            "yAxis": self.read_word_2c(0x45),
            "zAxis": self.read_word_2c(0x47)
        }
        return gyroscope_data

    def getRotData(self):
        accel_data = self.getAccData()
        rotation_data = {
            "xAxis": self.get_x_rotation(accel_data["xAxis"], accel_data["yAxis"], accel_data["zAxis"]),
            "yAxis": self.get_y_rotation(accel_data["xAxis"], accel_data["yAxis"], accel_data["zAxis"])
        }
        return rotation_data


sensor1 = Sensor(1, 0x68)
sensor2 = Sensor(1, 0x69)
sensor3 = Sensor(4, 0x68)
