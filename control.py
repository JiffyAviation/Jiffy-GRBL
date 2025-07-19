from serial_comm import send_gcode
import time

def unlock(grbl):
    send_gcode(grbl, "$X")

def home(grbl):
    send_gcode(grbl, "$H")

def laser_on(grbl, power=500):
    send_gcode(grbl, f"M3 S{power}")

def laser_off(grbl):
    send_gcode(grbl, "M5")

def move_absolute(grbl, x=None, y=None, feed=1000):
    if x is None and y is None:
        return
    cmd = "G90"
    send_gcode(grbl, cmd)
    move = "G1"
    if x is not None:
        move += f" X{x}"
    if y is not None:
        move += f" Y{y}"
    move += f" F{feed}"
    send_gcode(grbl, move)
