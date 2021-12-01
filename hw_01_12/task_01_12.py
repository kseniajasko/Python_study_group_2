from threading import Thread
from multiprocessing import Process

import requests
import os
from PIL import Image
import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            start_time = time.perf_counter()
            func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Функція {func.__name__}  виконана за {run_time:.4f} секунд")
        except RuntimeError as e:
            print(str(e))
    return wrapper

def load_image(url, save_image_name):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), save_image_name))

def rotate_image(file, degrees, name):
    image = Image.open(file)
    rotated = image.rotate(degrees, expand=True)
    rotated.save(name)

def write_to_file(file_name):
    string  = f"Hello winter!\n"
    path_json = os.path.join(os.getcwd(), 'data', file_name)
    with open(path_json, 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(string)
    f.close()

def delete_file(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError('No such file')

    if not os.path.isfile(file_name):
        raise IsADirectoryError("It's not file")

    os.remove(file_name)

@my_decorator
def load_image_threadind( ):
    URL1 = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
    URL2 = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
    URL3 = "https://media.wired.co.uk/photos/60c8730fa81eb7f50b44037e/3:2/w_3329,h_2219,c_limit/1521-WIRED-Cat.jpeg"

    thr1 = Thread(target=load_image, args=(URL1, "image1.jpg",))
    thr2 = Thread(target=load_image, args=(URL2, "image2.jpg",))
    thr3 = Thread(target=load_image, args=(URL3, "image3.jpg",))

    thr1.start()
    thr2.start()
    thr3.start()


@my_decorator
def rotate_image_threadind():
    thr1 = Thread(target=rotate_image, args=("image1.jpg", 90, "rotate1.jpg",))
    thr2 = Thread(target=rotate_image, args=("image2.jpg", 45, "rotate2.jpg",))
    thr3 = Thread(target=rotate_image, args=("image3.jpg", 180, "rotate3.jpg",))

    thr1.start()
    thr2.start()
    thr3.start()

@my_decorator
def write_to_file_threadind():
    thr1 = Thread(target=write_to_file, args=("text1.txt", ))
    thr2 = Thread(target=write_to_file, args=("text2.txt", ))
    thr3 = Thread(target=write_to_file, args=("text3.txt", ))

    thr1.start()
    thr2.start()
    thr3.start()

@my_decorator
def delete_to_file_threadind():
    thr1 = Thread(target=delete_file, args=("data/text1.txt", ))
    thr2 = Thread(target=delete_file, args=("data/text2.txt", ))
    thr3 = Thread(target=delete_file, args=("data/text3.txt", ))

    thr1.start()
    thr2.start()
    thr3.start()

@my_decorator
def load_image_multiproc():
    URL1 = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
    URL2 = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
    URL3 = "https://media.wired.co.uk/photos/60c8730fa81eb7f50b44037e/3:2/w_3329,h_2219,c_limit/1521-WIRED-Cat.jpeg"

    pr1 = Process(target=load_image, args=(URL1, "image1.jpg",))
    pr2 = Process(target=load_image, args=(URL2, "image2.jpg",))
    pr3 = Process(target=load_image, args=(URL3, "image3.jpg",))

    pr1.start()
    pr2.start()
    pr3.start()

    pr1.join()
    pr2.join()
    pr3.join()

@my_decorator
def rotate_image_multiproc():
    pr1 = Process(target=rotate_image, args=("image1.jpg", 90, "rotate1.jpg",))
    pr2 = Process(target=rotate_image, args=("image2.jpg", 45, "rotate2.jpg",))
    pr3 = Process(target=rotate_image, args=("image3.jpg", 180, "rotate3.jpg",))

    pr1.start()
    pr2.start()
    pr3.start()

    pr1.join()
    pr2.join()
    pr3.join()

@my_decorator
def write_to_file_multiproc():
    pr1 = Process(target=write_to_file, args=("text12.txt", ))
    pr2 = Process(target=write_to_file, args=("text22.txt", ))
    pr3 = Process(target=write_to_file, args=("text32.txt", ))

    pr1.start()
    pr2.start()
    pr3.start()

    pr1.join()
    pr2.join()
    pr3.join()

@my_decorator
def delete_to_file_multiproc():
    pr1 = Process(target=delete_file, args=("data/text12.txt", ))
    pr2 = Process(target=delete_file, args=("data/text22.txt", ))
    pr3 = Process(target=delete_file, args=("data/text32.txt", ))

    pr1.start()
    pr2.start()
    pr3.start()

    pr1.join()
    pr2.join()
    pr3.join()

@my_decorator
def load_image_noconcurent():
    URL1 = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
    URL2 = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
    URL3 = "https://media.wired.co.uk/photos/60c8730fa81eb7f50b44037e/3:2/w_3329,h_2219,c_limit/1521-WIRED-Cat.jpeg"

    load_image(URL1, "image1.jpg")
    load_image(URL2, "image2.jpg")
    load_image(URL3, "image3.jpg")

@my_decorator
def rotate_image_noconcurent():
    rotate_image("image1.jpg", 90, "rotate1.jpg")
    rotate_image("image2.jpg", 45, "rotate2.jpg")
    rotate_image("image3.jpg", 180, "rotate3.jpg")

@my_decorator
def write_to_file_noconcurent():
    write_to_file("text11.txt")
    write_to_file("text21.txt")
    write_to_file("text31.txt")

@my_decorator
def delete_to_file_noconcurent():
    delete_file("data/text11.txt")
    delete_file("data/text21.txt")
    delete_file("data/text31.txt")

if __name__ == "__main__":
    load_image_threadind()
    load_image_multiproc()
    load_image_noconcurent()
    rotate_image_threadind()
    rotate_image_multiproc()
    rotate_image_noconcurent()
    write_to_file_threadind()
    write_to_file_multiproc()
    write_to_file_noconcurent()
    delete_to_file_threadind()
    delete_to_file_multiproc()
    delete_to_file_noconcurent()


