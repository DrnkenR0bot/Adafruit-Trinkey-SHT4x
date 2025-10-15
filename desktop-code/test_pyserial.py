# test_pyserial.py
import serial
import serial.tools.list_ports

print(f"PySerial version: {serial.__version__}")

# List available ports
print("Available serial ports:")
ports = serial.tools.list_ports.comports()

if not ports:
    print("  No serial ports found")
else:
    for port in ports:
        print(f"  {port.device}: {port.description}")

# Test basic functionality
try:
    # This will fail if no port exists, but tests import
    ser = serial.Serial()
    print("✓ PySerial imported successfully")
    ser.close()
except Exception as e:
    print(f"⚠️  Warning: {e}")

