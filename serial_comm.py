import serial
import time

def connect_grbl(port='COM3', baudrate=115200, timeout=1):
    try:
        grbl = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)
        grbl.flushInput()
        print(f"✅ Connected to GRBL on {port}")
        return grbl
    except Exception as e:
        print(f"❌ Failed to connect to GRBL: {e}")
        return None

def send_gcode(grbl, command):
    try:
        grbl.write((command + '\n').encode())
        time.sleep(0.1)
    except Exception as e:
        print(f"❌ Error sending '{command}': {e}")
