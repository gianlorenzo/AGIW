import requests
import bs4


def takeUrl(url):
    source = requests.get(url).text
    return source


