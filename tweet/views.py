import threading
from datetime import datetime
from django.shortcuts import render
import tweepy

API_KEY = "I3aAe5ARoM1nn6Akwg0XRMjhR"
API_KEY_SECRET = "VogzNuih2s5YFcF0OuNcnDQlxd5TO2UuLpaI8Srpl22Cvzo3kv"
ACCESS_TOKEN = "1131789609543774208-6OfpHLqyZ6a7z25Paurgx71hU3YguS"
ACCESS_TOKEN_SECRET = "OqjBez1sBJD6gk3vyc5vtlwXUKxYvqATGBBuaKAI98OEn"

# Create your views here.


def fun(*tweet):
    print("Hey u called me")
    client = tweepy.Client(consumer_key=API_KEY,
                           bearer_token="AAAAAAAAAAAAAAAAAAAAAPaVXgEAAAAAadFYssMcyRwUSPuJOTHnDc8BAUE"
                                        "%3D1te4laG7pQZDeLd9iMKGsVFikwGynEMZOiH7Un5bTk9fPpexOn",
                           consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
    content = "".join(list(tweet))
    print(content)
    client.create_tweet(text=content)


def home(request):
    if request.method == 'POST':
        tweet = request.POST['tweet']
        timer = request.POST['time']

        reqTime = str(timer).split(":")
        currTime = str(datetime.now()).split(" ")[1].split(".")[0].split(":")
        hrsDiff = abs(int(reqTime[0]) - int(currTime[0]))
        minDiff = abs(int(reqTime[1]) - int(currTime[1]))
        delay = hrsDiff*60*60+minDiff*60
        start_time = threading.Timer(delay, fun, str(tweet))
        start_time.start()
    return render(request, 'index.html')
