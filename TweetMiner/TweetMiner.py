# -*- encoding: utf-8 -*-

'''
  TweetMiner Documentation
==========================

This TweetCrawler is a pet project I built on a lazy afternoon in my civil service. It'll eventually
be able to do several tasks related to twitter and twitter data, but for now it's a work in progress.

- Julius Rajala, 2015

 Controls
==========================

 Command       : Operation
==========================

gettimeline n : Gets n number of latest items from your timeline.
status        : Returns the number of API calls you have left on different 
                tasks.
exit          : Exit the application

'''

class TweetApp(object):
    def __init__(self):
        self.running = True

        self.consumer_key = s.consumer_key
        self.consumer_secret = s.consumer_secret
        self.access_token = s.access_token
        self.access_secret= s.access_secret
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)

        self.api = tweepy.API(self.auth)

        self.controls={ 
                        "gettimeline": self.timeLine,
                        "exit": self.quit,
                        "status":self.getStatus,
                        "stream":self.getStream
                        }
    
    def getStream(self, extra):
        streamlistener.main(self.auth, extra)

    def quit(self, extra):
        self.running = False

    def getStatus(self, extra):
        calls = self.api.rate_limit_status()
        for keys in calls:
            print keys + " : " + str(calls[keys])
            
            if keys == "rate_limit_context":
                print "Nothing here"
            else:
                print keys
                for a in keys:
                    print a + " : "+ keys[a]

    def run(self):
        while self.running:
            print "Calls remaining: " 
            command = raw_input(">> ").lower()
            command = command.split(" ")
            if command[0] in self.controls:
                self.controls[command[0]](command[1:] if len(command) >=2 else "Nothing here")


    def timeLine(self, amount):
        if amount is None:
            amount = 10
        for status in tweepy.Cursor(self.api.home_timeline).items(amount):
            try:
                print status.text + '\r\n'
            except:
                UnicodeEncodeError

if __name__ == "__main__":
    import tweepy
    from tweepy import OAuthHandler
    from lib import secrets as s
    import streamlistener
    
    print __doc__
    TweetApp().run()