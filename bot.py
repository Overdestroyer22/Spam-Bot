import pyautogui
import keyboard
import time
start = False;
message = input("Message: ")
counter = 1
print("press q to start")
while True:
    if start == True:
        break
    if keyboard.is_pressed('q'):
        start = True;
        print("start")
        time.sleep(0.5)
        pyautogui.hotkey('backspace')
while start == True:
#    if counter % 4 == 0:
#        counter = 1
#        if keyboard.is_pressed('q'):
#            start = False
#        time.sleep(2)

    #if counter % 2 == 0:
        #counter = 1
        #if keyboard.is_pressed('q'):
            #start = False
        #time.sleep(0.1)

    pyautogui.typewrite(message + "\n")
    #only if u wanna write commands IN DISCORD
    pyautogui.typewrite("\n")
    time.sleep(0)

    if keyboard.is_pressed('q'):
        start = False
    counter += 1