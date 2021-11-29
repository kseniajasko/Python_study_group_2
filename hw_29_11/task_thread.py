from PIL import Image
import requests
import threading
import os

URL1 = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
URL2 = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
URL3 = "https://media.wired.co.uk/photos/60c8730fa81eb7f50b44037e/3:2/w_3329,h_2219,c_limit/1521-WIRED-Cat.jpeg"
URL4 = "https://st3.depositphotos.com/1186248/14934/i/1600/depositphotos_149344592-stock-photo-open-sign-on." \
       "-a-window.jpg"
URL5 = "https://st2.depositphotos.com/3837271/5468/i/950/depositphotos_54688255-stock-photo-less-is-more-sign.jpg"

def load_image(url, save_image_name):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), save_image_name))

thr1 = threading.Thread(target=load_image, args=(URL1, "imageURL1.png",))
thr2 = threading.Thread(target=load_image, args=(URL2, "imageURL2.jpg",))
thr3 = threading.Thread(target=load_image, args=(URL3, "imageURL3.jpg",))
thr4 = threading.Thread(target=load_image, args=(URL4, "imageURL4.jpg",))
thr5 = threading.Thread(target=load_image, args=(URL5, "imageURL5.jpg",))

thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr5.start()