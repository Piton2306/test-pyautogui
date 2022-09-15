import time
# import mouseinfo
# mouseinfo.mouseInfo()
import pyautogui
pyautogui.hotkey('alt', 'shift')
pyautogui.moveTo(289,53, duration=0, tween=pyautogui.easeInOutQuad)
pyautogui.tripleClick()
pyautogui.write('Hello world!', interval=0)
pyautogui.tripleClick()
pyautogui.moveTo(289,53, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.hotkey('ctrl', 'c')
pyautogui.rightClick()
# pyautogui.moveTo(100, 150)
# pyautogui.write('Hello world!', interval=0.25)
print()
