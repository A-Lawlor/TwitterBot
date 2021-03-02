__author__ = 'Anthony Lawlor'
import pyowm
import tweepy
import datetime
import os
from os import environ

#Twitter API Codes
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCCESS_SECRET']

#Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Weather API
City = 'Lowell'
APIKEY='f76ac8987e6e5d283f48db6929705767'
OpenWMap=pyowm.OWM(APIKEY)
Weather=OpenWMap.weather_at_place(City)
Data=Weather.get_weather()
Detailed = Data.get_detailed_status() # get status with more detailed  eg: light rain
wind = Data.get_wind()
Wind = wind['speed']
temp = Data.get_temperature(unit='fahrenheit')
Temp = str(temp['temp'])

deg = u'\xb0'


FullWeather = 'Over-View: ' + str(Detailed) + "\n" + 'Temperature: ' + Temp + deg + "F\n" + 'Wind-Speed: ' + str(Wind) +"mph"



def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = '#TwitterBot Hello everyone today is Monday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 1:
        tweettopublish = '#TwitterBot Hello everyone today is Tuesday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 2:
        tweettopublish = '#TwitterBot Hello everyone today is Wednesday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 3:
        tweettopublish = '#TwitterBot Hello everyone today is Thursday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 4:
        tweettopublish = '#TwitterBot Hello everyone today is Friday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 5:
        tweettopublish = '#TwitterBot Hello everyone today is Saturday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather
    if datetime.date.today().weekday() == 6:
        tweettopublish = '#TwitterBot Hello everyone today is Sunday\n' + 'The Weather Forcast in ' + City +", MA today is: \n"  + FullWeather

    api.update_status(tweettopublish)
    print(tweettopublish)

publictweet()
