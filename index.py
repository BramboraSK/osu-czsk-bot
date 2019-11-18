import tweepy
import random
import requests
import threading

//API
auth = tweepy.OAuthHandler("...", "...")
auth.set_access_token("...", "...")

api = tweepy.API(auth)

//Súbory
hraci = open("hraci.txt").readlines()
pridavne_mena = open("pridavne_mena.txt").readlines()

def send():
    //Tweet každých 1200 sekúnd (20 minút)
    threading.Timer(1200.0, send).start()
    
    api.update_status(random.choice(hraci).replace("\n", "") + " je " + random.choice(pridavne_mena).replace("\n", ""))

send()
