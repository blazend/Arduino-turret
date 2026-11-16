# Arduino-turret
Mouse controlled laser turret and a gesture bot that reacts to discord messages 

Version A:
- A laser turret controlled by mouse(if you know Michael Reeves this is basically it)
  




https://github.com/user-attachments/assets/1fedfe59-efc3-48d7-8fd1-dcdf24560a31



Version B:
- Does preprogrammed gestures depending on discord messages
  Right now there's 2 gestures a "Nod" and a "Headshake" depending if a message contains "yes" or "no"(not case sensitive)
- Also uses talking Ben voice lines very goofy ahh

https://github.com/user-attachments/assets/eeaec696-3d51-4f5c-a748-b5543b6e3b4e
  


## Hardware
- Arduino (any)
- 2x SG90 servos (yaw and pitch)
- Laser module
- USB cable for serial connection

- ## Wiring
- Pan/yaw servo → Pin 9
- Tilt/pitch servo → Pin 10
- <img width="739" height="608" alt="image" src="https://github.com/user-attachments/assets/ea91a41e-491a-48f8-881e-e352a104a528" />


## Files
- `turret.ino` this needs to be loaded on the Arduino first before using the other python files
- `turret.py` — mouse control
- `discord_bot.py` — Discord bot


## Troubleshooting
- IF IT DOESN'T WORK ensure you did step 3

## Setup
1. Install dependencies:
   pip install pyserial pyautogui discord.py pygame python-dotenv

2. Setup your bot:
   watch this short video on how to do that
   https://www.youtube.com/watch?v=2jOzQWnKc-o

3. Set the correct serial port in the script (`/dev/ttyUSB0` on Linux, 
   `COM3`-ish on Windows
4. Run either script depending on what you want

## Notes
- Currently listens to all channels the bot is in
- Sound files go in an `assets/` folder
