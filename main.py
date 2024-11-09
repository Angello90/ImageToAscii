from src import *
import argparse
from PIL import Image




def main(image_path, scale, output_file):
        image = Image.open(image_path)
        image = resize_image(image, scale)
        image = to_grayscale(image)
        
        ascii_str = pixels_to_ascii(image)
        img_width = image.width
        ascii_str_len = len(ascii_str)
        ascii_img = "\n".join([ascii_str[index:(index + img_width)] for index in range(0, ascii_str_len, img_width)])
        with open(output_file, "w") as f:
            f.write(ascii_img)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert any image into ASCII art")
    parser.add_argument("-i", "--image", help="Image file path", required=True)
    parser.add_argument("-s", "--scale", type=int, help="Scale down the image", default=10)
    parser.add_argument("-o", "--output", help="Output file name", default="output.txt")
    args = parser.parse_args()
    image_path = args.image
    scale_args = args.scale
    out_file = args.output
    main(image_path, scale_args, out_file)