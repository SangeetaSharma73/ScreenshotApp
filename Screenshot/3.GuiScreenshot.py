import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import os
import playsound

def capture_screenshots(url, save_path, folder_name):
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(3)

    height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    num_chunks = height // viewport_height + 1

    screenshots = []

    for i in range(num_chunks):
        screenshot = driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        screenshots.append(screenshot)
        
        if i < num_chunks - 1:
            driver.execute_script("window.scrollTo(0, window.scrollY + window.innerHeight);")
            time.sleep(0.5)

    driver.quit()
    
    folder_path = os.path.join(save_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for i, screenshot in enumerate(screenshots):
        screenshot_path = os.path.join(folder_path, f"screenshot_{i+1}.png")
        screenshot.save(screenshot_path)
    
    playsound.playsound('welcome.mp3')
    print("Screenshots saved successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    save_path_var.set(folder_selected)

def take_screenshots():
    url = url_var.get()
    save_path = save_path_var.get()
    folder_name = folder_name_var.get()
    
    if not url or not save_path or not folder_name:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    capture_screenshots(url, save_path, folder_name)
    messagebox.showinfo("Success", "Screenshots saved successfully!")

# Create the main window
root = tk.Tk()
root.title("Webpage Screenshot Tool")
root.geometry("500x300")

# URL input
tk.Label(root, text="Enter the URL of the webpage:").pack(pady=10)
url_var = tk.StringVar()
tk.Entry(root, textvariable=url_var, width=50).pack()

# Save path input
tk.Label(root, text="Select the path to save screenshots:").pack(pady=10)
save_path_var = tk.StringVar()
tk.Entry(root, textvariable=save_path_var, width=50).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

# Folder name input
tk.Label(root, text="Enter the folder name to save screenshots:").pack(pady=10)
folder_name_var = tk.StringVar()
tk.Entry(root, textvariable=folder_name_var, width=50).pack()

# Capture button
tk.Button(root, text="Capture Screenshots", command=take_screenshots).pack(pady=20)

root.mainloop()
