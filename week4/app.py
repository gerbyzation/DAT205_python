import twitter
import datetime
import re
import urllib2
from bs4 import BeautifulSoup

file = open('auth.txt')
keys = file.readline().strip().split(',')

historyFile = open("/Users/gerbenneven/Library/Application Support/Google/Chrome/Default/Current Session")
history = historyFile.read()
historyFile.close()

start = history.rfind('http')
end = history.find(chr(0), start)
url = history[start:end]

page = urllib2.urlopen(url)
body = page.read()

soup = BeautifulSoup(body)
title = soup.html.head.title.contents
print(url)
print(title)

# urls = re.findall("http[s]?://[a-zA-Z]|[0-9]|[.]/", history)


api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2], access_token_secret=keys[3])

response = api.PostUpdate("I'm a python script and we have taken over! #Pyton #DAT205")

print("Status posted:s " + response.text)
