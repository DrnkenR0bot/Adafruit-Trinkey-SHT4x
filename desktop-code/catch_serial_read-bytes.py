import serial
import serial.tools.list_ports
import sys

print(f"PySerial version: {serial.__version__}")

# List available ports
print("Available serial ports:")
ports = serial.tools.list_ports.comports()

if not ports:
    print("  No serial ports found")
else:
    for port in ports:
        print(f"  {port.device}: {port.description}")
        #print(dir(port))

#sys.exit(0)

read_size = 8 # bytes
ser = serial.Serial(port.device, 9600, timeout=5)
print(f"Ready to read {read_size} bytes of serial communication...")

# Read read_size number of bytes
data = ser.read(read_size)
print(f"Read {len(data)} bytes: {data}")

# Read single byte
byte = ser.read(1)
if byte:
    print(f"Got byte: {byte[0]:02X}")