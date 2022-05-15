import os
import requests
from dotenv import load_dotenv

load_dotenv()

session = requests.Session()


def wiki_request(url, use_proxies=False):
    if use_proxies:
        http_proxy = os.getenv('http_proxy')
        https_proxy = os.getenv('https_proxy')

        proxies = {
            "http": http_proxy,
            "https": https_proxy,
        }
        return requests.get(url, proxies=proxies, headers={
            "User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"})
    try:
        return requests.get(url)
    except Exception as e:
        print(e)
