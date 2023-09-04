import pyautogui

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

#button_x, button_y = pyautogui.locateCenterOnScreen('create_button.png')
#pyautogui.click(button_x, button_y)

# mouse movement
pyautogui.moveTo(100,100,duration=2)
pyautogui.moveRel(200,0,duration=2)

# click
pyautogui.click(100,100)
pyautogui.doubleClick(100,100)
pyautogui.rightClick(100,100)

# drag
pyautogui.dragTo(100,100,duration=2)
pyautogui.dragRel(200,0,duration=2)

# scroll
pyautogui.scroll(200)

# keyboard
pyautogui.typewrite('Hello world!')
pyautogui.press('enter')
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

# screenshot
im1 = pyautogui.screenshot()
im1.save('im1.png')

# locate
pyautogui.locateOnScreen('im2.png')
pyautogui.locateCenterOnScreen('im2.png')

# hotkey
pyautogui.hotkey('ctrl','o').typewrite('Hello world!', interval=0.25)

# Press the Home key.
pyautogui.press('home')