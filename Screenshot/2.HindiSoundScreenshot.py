from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import os
import playsound
import gtts
from gtts import gTTS

# Take URL input from the user
url = input("Enter the URL of the webpage: ")

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # You need to have Chrome webdriver installed

# Open the webpage
driver.get('about:blank')  # Open a blank page first

# Get the height of the webpage
driver.get(url)
time.sleep(3)  # Wait for 3 seconds for the page to load (adjust as needed)

# Get the height of the webpage
height = driver.execute_script("return document.body.scrollHeight")

# Set the initial position and chunk height
position = 0
chunk_height = driver.execute_script("return window.innerHeight")

# Container for storing screenshots
screenshots = []

# Scroll and capture screenshots until reaching the bottom
while position < height:
    # Scroll to the current position
    driver.execute_script(f"window.scrollTo(0, {position});")
    time.sleep(0.5)  # Optional: Add a small delay for the page to stabilize
    
    # Capture screenshot of the current view
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    screenshots.append(screenshot)
    
    # Move to the next position
    position += chunk_height

# Close the webdriver
driver.quit()

# Ask user for the path to save screenshots and folder name
save_path = input("Enter the path to save screenshots (e.g., /path/to/desktop): ")
folder_name = input("Enter the folder name to save screenshots: ")
folder_path = os.path.join(save_path, folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save each screenshot as an image file
for i, screenshot in enumerate(screenshots):
    screenshot_path = os.path.join(folder_path, f"screenshot_{i+1}.png")
    screenshot.save(screenshot_path)

# Generate speech for "Screenshots saved successfully!"
# tts = gTTS(text='Screenshots saved successfully!', lang='en')
# tts.save(os.path.join(folder_path, 'success.mp3'))
playsound.playsound('welcome.mp3')
print("Screenshots saved successfully!")
