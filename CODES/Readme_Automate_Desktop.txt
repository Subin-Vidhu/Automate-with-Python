Automate Desktop (notes)
Pyautogui is a great library for automating GUI interactions. It's really easy to use and it's cross platform, so it works on Windows, Mac, and Linux.

To install pyautogui, just run

pip install pyautogui 
from the terminal. pyautogui is not the only module for this, but it is one that works on every popular computer system.

Once it's installed, we can import it into our Python script like so:

import pyautogui
Let's say we want to put the mouse in the center of the screen, you can do this:

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
If you run it, Python will then move the mouse on your computer to the center of the screen.

Now let's say we want to automate clicking the 'Create' button in a web application. We can do that with just a few lines of code:

button_x, button_y = pyautogui.locateCenterOnScreen('create_button.png')
pyautogui.click(button_x, button_y)
First we use the locateCenterOnScreen() function to find the x and y coordinates of the button on the screen. Then we use the click() function to click on that location.

That's all there is to it! With just a few lines of code, we can automate clicking on buttons, filling out form fields, and much more. So let's see what else we can do.

You can move the mouse on the screen automatically. Here we use XY coordinates. XY coordinates have origin at top left corner of the screen. X increases going right, Y increases going down.

# mouse movement
pyautogui.moveTo(100,100,duration=2)
pyautogui.moveRel(200,0,duration=2)
If duration is 0 or unspecified, movement is immediate.

It can click on automatically

# click
pyautogui.click(100,100)
pyautogui.doubleClick(100,100)
pyautogui.rightClick(100,100)
You can drag

# drag
pyautogui.dragTo(100,100,duration=2)
pyautogui.dragRel(200,0,duration=2)
Do mouse scrolling

# scroll
pyautogui.scroll(200)
But you are not limited to automating the mouse, you can do the keyboard too:

# keyboard
pyautogui.typewrite('Hello world!')
pyautogui.press('enter')
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')
You can make it take screenshots

# screenshot
im1 = pyautogui.screenshot()
im1.save('im1.png')
It can locate things on the screen

# locate
pyautogui.locateOnScreen('im2.png')
pyautogui.locateCenterOnScreen('im2.png')
You can use hot keys

# hotkey
pyautogui.hotkey('ctrl','o').typewrite('Hello world!', interval=0.25)
and you can make it press any key you want

# Press the Home key.
pyautogui.press('home')
So you can use a Python script to automate any task on the computer.

Here's an example of what a script may look like:

import pyautogui
 
# Move the mouse to the coordinates (100, 200)
pyautogui.moveTo(100, 200)
 
# Move the mouse relative to its current position
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
 
# Get the current mouse position
currentMouseX, currentMouseY = pyautogui.position()
 
# Click the left mouse button
pyautogui.click()
 
# Double click the left mouse button
pyautogui.doubleClick()
 
# Drag the mouse from (100, 200) to (300, 400)
pyautogui.dragTo(300, 400, duration=0.25)
 
# Type "Hello World!"
pyautogui.typewrite('Hello World!', interval=0.25)
 
# Press the key combination "Ctrl+C"
pyautogui.hotkey('ctrl', 'c')
Of course it depends on which task you want to automate.

One of the challenges in this type of automation is dealing with change. Companies can update their websites, web apps or software making it completely look different. If they move a button, change an image or make other visual modifications, it might break your script.

So pyautogui is a great way to automate desktop apps or even web app, for web apps it's still better to use an API. That is because the company can change what the website looks like any time, if it would use the GUI only then your script wouldn't work anymore. But, it's possible to automate anything on the desktop this way.

Because applications may look different, it could be that you need to make different scripts for every platform. But this completely depends on appearance. One way to get around that is by using the keyboard shortcuts instead. Overall keyboard shortcuts almost never change.