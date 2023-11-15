import requests

image_file = r'C:\Users\shameer\Desktop\Trogonmedia Assessment\screenshotapi-dev\assets\images\cloud.jpg'

def send_to_api(image_file=None, remarks=None, phone=None):

    """
    Takes an image file-path, remarks and phone and then returns the API response.

    Parameters:
    - image_path (str): The path to the image.
    - remarks and phone: User-provided fields for API submission.

    Returns: The API response.
    """

    api = "https://trogon.info/interview/python/index.php"
       
    files = {
        'image': open(image_file, 'rb') 
    }
    
    payload = { 
        "remarks": f"{remarks}",
        "phone": f"{phone}"
        }
    
    response = requests.post(api, files=files, data=payload,)
    try:
        data = response.json()     
        return data               
    except requests.exceptions.RequestException:
        return response.text