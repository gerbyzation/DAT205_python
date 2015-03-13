import twitter
import datetime

user = 214990133

file = open('auth.txt')
keys = file.readline().strip().split(',')

api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2], access_token_secret=keys[3])

response = api.PostUpdate("I'm a python script and we have taken over! #Pyton #DAT205")

print("Status posted:s " + response.text)
