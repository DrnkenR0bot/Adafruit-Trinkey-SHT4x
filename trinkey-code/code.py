import time
import board
import adafruit_sht4x

send_interval = 5*60 # seconds

def C2F(c):
    """Convert Centigrade to Fahrenheit"""
    return (1.8*c + 32.)

i2c = board.I2C()  # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

while True:
    temperature, relative_humidity = sht.measurements
    temperature = C2F(temperature)
    print(f"{temperature:0.0f}/{relative_humidity:0.0f}")
    time.sleep(send_interval)
