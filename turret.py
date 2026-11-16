import serial
import time
import pyautogui 


# Make the port equal to something like COM3 or COM5 etc if on windows 
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=8000, timeout=0.1)
time.sleep(2)

print("Turret Control Active! Move your mouse to aim.")

try:
    while True:
        # Get mouse X and Y
        mouseX, mouseY = pyautogui.position()
        # print(pyautogui.position())

        # Get your screen size
        width, height = pyautogui.size()

        # Map screen pixels to Servo degrees (0-180)
        # We invert Y (180 - ...) so moving mouse up tilts the laser up
        x_angle = int(180 - (mouseX / width) * 180)
        y_angle = int(180 - (mouseY / height) * 180)

        
        arduino.write(bytearray([x_angle, y_angle]))

        time.sleep(0.02) 

except KeyboardInterrupt:
    print("Stopping...")
    arduino.close()
