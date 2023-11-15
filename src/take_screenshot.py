import pyautogui
import os
import secrets
import string

def generate_random_filename(length=4):

    """
    Function used as a helper inorder to generate unique random filenames.
    """
    
    characters = string.ascii_letters + string.digits
    random_filename = ''.join(secrets.choice(characters) for _ in range(length))
    return f"{random_filename}.png"

def take_screenshot():
    
    """
    Takes the screenshot and returns the image path.
    """
    
    screen_width, screen_height = pyautogui.size()

    screenshot = pyautogui.screenshot()

    dir_path = os.path.join(os.getcwd(), 'assets', 'images')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    filename = generate_random_filename()
    output_filename = os.path.join(dir_path, filename)

    screenshot.save(output_filename)
    return output_filename



