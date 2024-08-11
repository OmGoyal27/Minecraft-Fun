import pyautogui as pg
import keyboard

#pg.FAILSAFE = False
isMode_on_shift = False
isMode_on_clicker = False
checkIfItIsPressedAlready = False

# Define a callback function that will be called when the key is pressed
def on_key_press_shift(e):
    global isMode_on_shift
    if isMode_on_shift:
        isMode_on_shift = False
    else:
        isMode_on_shift = True

# Set up the listener for a specific key
keyboard.on_press_key('down', on_key_press_shift)

# Define a callback function that will be called when the key is pressed
def on_key_press(e):
    global isMode_on_clicker
    if isMode_on_clicker:
        isMode_on_clicker = False
    else:
        isMode_on_clicker = True

# Set up the listener for a specific key
keyboard.on_press_key('up', on_key_press)

while True:
    if isMode_on_clicker:
        pg.rightClick()

    if isMode_on_shift:
        pg.hold("shiftleft")
    else:
        pg.keyUp("shiftleft")

