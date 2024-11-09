ASCCI_CHARS = ["@", "#", "$", "%", "?", "*", "'", ";", ":", ",", "."]

def resize_image(image, scale=100):
    width, height = image.size
    aspect_ratio = height / width
    new_width =  int((width *aspect_ratio) // scale);
    new_height = int((height *aspect_ratio) // scale);
    # new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
        grayscale_image = image.convert("L")
        return grayscale_image

def pixels_to_ascii(image):
        pixels = image.getdata()
        ascii_str = "".join([ASCCI_CHARS[pixel // 25] for pixel in pixels])
        return ascii_str