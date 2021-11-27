import  threading
import time
import requests

def open_url(url):
    print(f'Got url {url}')
    resp = requests.get(url)
    print(url, resp.status_code)

thr1 = threading.Thread(target=open_url, args=('https://google.com.ua', ))
thr2 = threading.Thread(target=open_url, args=('https://en.wikipedia.org', ))
thr3 = threading.Thread(target=open_url, args=('https://rozetka.ua', ))

thr1.start()
thr2.start()
thr3.start()