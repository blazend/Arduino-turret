# Arduino-turret
There's 2 versions of this turret using the same Arduino code but 2 python files 

Version A:
- A laser turret controlled by mouse(if you know Michael Reeves this is basically it)

Version B:
- Does preprogrammed gestures depending on discord messages
  Right now there's 2 gestures a "Nod" and a "Headshake" depending if a message contains "yes" or "no"(not case sensitive)


## Hardware
- Arduino (any)
- 2x SG90 servos (yaw and pitch)
- Laser module
- USB cable for serial connection

- ## Wiring
- Pan/yaw servo → Pin 9
- Tilt/pitch servo → Pin 10

## Files
- `turret.ino` this needs to be loaded on the Arduino first before using the other python files
- `turret.py` — mouse control
- `discord_bot.py` — Discord bot


## Setup
1. Install dependencies:
   pip install pyserial pyautogui discord.py pygame python-dotenv

2. Setup your bot:
   watch this short video on how to do that
   https://www.youtube.com/watch?v=2jOzQWnKc-o

3. Set the correct serial port in the script (`/dev/ttyUSB0` on Linux, 
   `COM3`-ish on Windows)
   
5. Run either script depending on what you want

## Notes
- Currently listens to all channels the bot is in
- Sound files go in an `assets/` folder
