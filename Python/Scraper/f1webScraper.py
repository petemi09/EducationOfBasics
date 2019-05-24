# import libraries

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://web.mta.info/developers/turnstile.html"
response = requests.get(url)
print(response)