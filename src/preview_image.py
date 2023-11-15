from PIL import Image

def preview_image(image_path):
    
    """
    Previews the image
    """

    Image.open(image_path).show()