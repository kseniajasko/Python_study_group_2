#run `pip install pillow` before
#make sure you have `requests` lib installed
#use https://pillow.readthedocs.io/en/stable/handbook/tutorial.html for reference

from PIL import Image
import requests
import os


URL = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"

def load_image(url):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), "img1.jpg"))

def print_imaged_data(file):
    image = Image.open(file)
    print(image.size, image.mode)

def is_square_image(file):
    image = Image.open(file)
    return not image.size[0] != image.size[1]

def create_thumbnail(file):
    #TODO: handle all errors on thumbnail creation

    if not file.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
        raise FileNotFoundError("Wrong file extension ")

    if not os.path.isfile(file):
        raise FileNotFoundError("File not exist")

    thumbnail_size = (200, 200)
    image = Image.open(file)
    image.thumbnail(thumbnail_size)
    image.save("thumbnail.jpg", "JPEG")

def is_thumbnail(file):
    thumbnail_size = [200, 200]
    image = Image.open(file)
    return image.size == thumbnail_size

def rotate_image(file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees, expand=True)
    rotated.save("rotated.jpg")

def flip_image(file, direction):
    directions = {"LR": Image.FLIP_LEFT_RIGHT, "TB": Image.FLIP_TOP_BOTTOM}
    image = Image.open(file)
    out = image.transpose(directions[direction])
    out.save("flipped.jpg")

def copy_images_to_dir(dirname):
    '''Copies all images from current folder into subfolder'''

    for file in os.listdir():
        if file.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))

def delete_images(file_name):
    for file in os.listdir():
        if file.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")):
            if file == file_name:
                os.remove(file_name)
                return f"File {file_name} removed"
    return f"File {file_name} isn't found"

def create_rectangle(file_name, tmp_tuple):
    image = Image.open(file_name)
    out = image.crop(tmp_tuple)
    out.save("rectangle.jpg", quality=95)

# if __name__ == "__main__":
#     create_rectangle("img1.jpg", (1000, 1750, 3000, 2500))
#     load_image(URL)
#     print_imaged_data("img1.jpg")
#     print(is_square_image("img1.jpg"))
#     create_thumbnail("img2.jpg")
#     is_thumbnail("thumbnail.jpg")
#     rotate_image("img1.jpg", 45)
#     flip_image("img1.jpg", "LR")
#     copy_images_to_dir("images")
#     print(delete_images("img2.png"))
#     print("Done!")