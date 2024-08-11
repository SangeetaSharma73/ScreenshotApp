import pyautogui
import tkinter as tk
from tkinter.filedialog import *
root=tk.Tk()
window=tk.Canvas(root,width=200,height=200)
window.pack()
def take_screenshot():
    screenshot=pyautogui.screenshot()
    save_path=asksaveasfilename()
    screenshot.save(save_path+'_screenshot.png')
ss_button=tk.Button(text="Take Screenshot",command=take_screenshot,font=15)
window.create_window(100,100,window=ss_button)
root.mainloop()