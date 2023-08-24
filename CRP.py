import threading
import time
import secrets
import string
import pyperclip
import pystray
from PIL import Image
from pystray import Icon, Menu, MenuItem
import keyboard
import pyautogui

def CreateRandomPass(length):
    alphabet = string.ascii_letters
    digits = string.digits
    symbols = str(set(string.punctuation) - set(['<', '>', ' ' ]))
    password = [
        secrets.choice(alphabet),
        secrets.choice(alphabet.lower()),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    while len(password) < length:
        password.append(secrets.choice(alphabet + digits + symbols))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def quit_app(icon, item):
    icon.stop()

def on_key_release(event):
    if event.name == "insert":
        RandomPass = CreateRandomPass(8)
        pyperclip.copy(RandomPass)
        pyautogui.press("nonconvert")
        pyautogui.write(RandomPass)
    elif event.name == "home":
        quit_app(icon, None)

def background_loop():
    keyboard.on_release(on_key_release)

image = Image.open("logo.ico")
menu = Menu(
    MenuItem('Quit', quit_app)
)
icon = pystray.Icon("CreateRandomPass", icon=image, title="CRP", menu=menu)
icon_thread = threading.Thread(target=icon.run)
icon_thread.start()

background_thread = threading.Thread(target=background_loop)
background_thread.start()