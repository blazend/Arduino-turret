import asyncio
import random
import serial
import time
import discord
import pygame

# Initialize pygame mixer
pygame.mixer.init()
sound_files = ["assets/Hohohoho.mp3", "assets/Talking Ben No.mp3"]
sound_list = [pygame.mixer.Sound(f) for f in sound_files]
yes = pygame.mixer.Sound("assets/Yes_.mp3")

# Initialize Serial connection to Arduino
# (Make sure to wrap arduino.write in a try/except block if your hardware isn't always plugged in)
# Make the port equal to something like COM3 or COM5 etc if on windows 
try:
  arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=8000, timeout=0.1)
  time.sleep(2)
except Exception as e:
  print(f"Warning: Serial connection failed: {e}")
  arduino = None

# Global angles
x_angle = 90
y_angle = 90

# Setup Discord Intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def nod():
  global y_angle
  yes.play()
  nod_sequence = [90, 45, 90]
  for target_y in nod_sequence:
    y_angle = target_y
    if arduino and arduino.isOpen():
      arduino.write(bytearray([x_angle, y_angle]))
    await asyncio.sleep(0.3) 


async def head_shake():
  global x_angle
  random.choice(sound_list).play()
  shake_sequence = [90, 60, 120, 60, 120, 90]
  for target_x in shake_sequence:
    x_angle = target_x
    if arduino and arduino.isOpen():
      arduino.write(bytearray([x_angle, y_angle]))
    await asyncio.sleep(0.15)  


@client.event
async def on_ready():
  print(f"Connected and listening as {client.user}")


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself 
    if message.author == client.user:
        return

    print(f"Signal received from {message.author}: {message.content}")

    # Trigger physical action when a message arrives
    if "yes".casefold() in message.content.casefold():
        await nod()  
    elif "no".casefold() in message.content.casefold():
        await head_shake()




client.run("PUT YOUR BOT TOKEN HERE")
