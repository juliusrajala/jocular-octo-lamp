# -*- encoding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler

import secrets as s

'''
TweetBot Documentation
======================

This TweetCrawler is a pet project I built on a lazy afternoon in my civil service. It'll eventually
be able to do several tasks related to twitter and twitter data, but for now it's a work in progress.

- Julius Rajala, 2015

Controls
========

Command             Operation

GetTimeLine n   :   Gets n number of latest items from your timeline.

'''

class TweetApp(object):
    def __init__(self):
        self.consumer_key = s.consumer_key
        self.consumer_secret = s.consumer_secret
        self.access_token = s.access_token
        self.access_secret= s.access_secret
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)

        self.api = tweepy.API(self.auth)

        self.controls={ 
                        "gettimeline": self.timeLine
                        
                        }

    def run(self):
        while running:
            command = raw_input(">").lower()
            command = command.split(" ")
            if command[0] in controls:
                controls[command[0]](command[1:])


    def timeLine(self, amount):
        if amount is None:
            amount = 10
        for status in tweepy.Cursor(self.api.home_timeline).items(amount):
            try:
                print status.text + '\r\n'
            except:
                UnicodeEncodeError

if __name__ == "__main__":
    TweetApp().run()