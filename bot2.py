import pyautogui
import keyboard
import time
import random
import pyperclip

start = False
enter = ""
range1 = int(input("Lower range: "))
range2 = int(input("Upper range: "))
while True:
    if enter == "Y" or enter == "N":
        break
    else:
        enter = input("Enter or no(Y or N): ")
length = int(input("Amount of random chars for each loop: "))
t = int(input("Amount of time between each loop: "))
print("press q to start")
while True:
    if start:
        break
    if keyboard.is_pressed('q'):
        start = True;
        print("start")
        time.sleep(0.5)

while start:
    message = ""
    while len(message) < length:
        r = random.randint(range1, range2)
        message = chr(r) + message
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    if enter == "Y":
        pyautogui.typewrite("\n")
        pyautogui.typewrite("\n")
    time.sleep(t)
    if keyboard.is_pressed('q'):
        start = False