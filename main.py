import tkinter as tk
import time

from src.take_screenshot import take_screenshot
from src.preview_image import preview_image
from src.send_to_api import send_to_api

class ScreenshotApp:
    """
    A class that encapsulates functions related to taking screenshots and posting in to
    an endpoint along with the required fields.

    Functions:
    - take_screenshot: Captures a screenshot and saves it in the assets\images directory, previews it.
    - send_to_api: Takes the screenshot, other fields and returns the API response.

    Example Usage:
    >>> screenshotapi = ScreenshotApp()
    >>> screenshotapi.take_screenshot()
    >>> screenshotapi.preview_screenshot()
    >>> response = screenshotapi.send_to_api(image_path='assets/images/screenshot.png',
                                           remarks = 'remarks', phone = 'phone')
    print(response)
    """
    def __init__(self, root):

        """
        Initializes the ScreenshotApp.
        """
         
        self.root = root
        self.root.title("Screenshot App")

        self.image_path = None

        tk.Label(root, text="Stay on the screen where you want take the shot!").pack(pady=10)

        # Buttons
        self.screenshot_button = tk.Button(root, text="Take Screenshot", command=self.get_screenshot)
        self.screenshot_button.pack(pady=10)


        # Entry fields
        tk.Label(root, text="Remarks:").pack(pady=5)
        self.remarks_entry = tk.Entry(root, width=30)
        self.remarks_entry.pack(pady=5)

        tk.Label(root, text="Phone:").pack(pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack(pady=5)

        # Send API
        self.send_button = tk.Button(root, text="Send to API", command=self.submit_to_api)
        self.send_button.pack(pady=10)

        # Response box
        tk.Label(root, text="API Response:").pack(pady=5)
        self.response_text = tk.Text(root, height=5, width=40)
        self.response_text.pack(pady=10)

        
    def get_screenshot(self):

        """
        Captures a screenshot, saves it in the assets/images directory and previews it.
        """

        self.root.iconify()
        time.sleep(2)
        self.image_path = take_screenshot()
        self.root.deiconify()
        return preview_image(self.image_path)
            
    def submit_to_api(self):

        """
        Calls the function send_to_api which takes an image path and user-provided fields, 
        then returns the API response.
        """

        remarks = self.remarks_entry.get()
        phone = self.phone_entry.get()

        if not any([remarks,phone,self.image_path]):
            self.response_text.insert(tk.END, "Field missing values. Please check the image, remarks and phone values.\n")
            return

        api_response = send_to_api(image_file=self.image_path, remarks=remarks, phone=phone)
        self.response_text.insert(tk.END, f"API Response: {api_response}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
