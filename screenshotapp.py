import pyautogui
import time
import tkinter as tk


def screenshot ():
  time.sleep(5)
  name = int(round(time.time()*1000))
  name = 'C:/Users/JitendraSaroj/Desktop/ScreenshotApp/output/{}.png'.format(name)
  img = pyautogui.screenshot(name)
  img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button (
  frame,
  text = "ScreenShot",
  command = screenshot
)
button.pack(side =tk.LEFT)
button = tk.Button (
  frame,
  text = "Quit",
  command = quit
)
button.pack(side =tk.LEFT)
root.mainloop()