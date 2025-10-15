import serial
import serial.tools.list_ports
import time
import requests
from secrets import USERNAME, AIOKEY

# https://www.pyserial.com/docs/reading-data
# documents different end character lines

print(f"PySerial version: {serial.__version__}")

# List available ports
print("Available serial ports:")
ports = serial.tools.list_ports.comports()

if not ports:
    print("  No serial ports found")
else:
    for port in ports:
        print(f"  {port.device}: {port.description}")

# Read until \r\n or \n end line character.
ser = serial.Serial(port.device, 9600, timeout=10)

def readline():
    line = ser.readline()
    text = line.decode('utf-8').strip()
    if len(text) == 0:
        return None
    else:
        #print(f"Received: {text}")
        parsed = text.split("/")
        if len(parsed) == 2:
            return tuple(parsed)
        else:
            return None

def send_data(feed, value):
    """ Fault tolerant HTTP send using requests.post() """
    url = f"https://io.adafruit.com/api/v2/{USERNAME}/feeds/{feed}/data"
    headers = {
        "X-AIO-Key": AIOKEY
    }
    if type(value) != type({}): # check to see if 'value' is already a dict
        data = {
            'value': value
        }
    else:
        data = value
    try:
        response = requests.post(url, headers=headers, data=data)
        status_code = response.status_code
    except Exception as e:
        print("POST ERROR: {e}")
        return False
    if status_code == 200:
        print(f"{feed} data value={value} successfully sent to Adafruit IO")
        return True
    else:
        print("Failed to send data. Code restart recommended.")
        return False

while True:
    intercept = readline()
    if intercept != None:
        (temperature, humidity) = intercept
        send_data("lws.temperature-test", temperature)
        send_data("lws.humidity-test", humidity)
    time.sleep(10)
