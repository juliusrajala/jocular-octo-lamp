# -*- encoding: utf-8 -*-


class TweetApp(object):
    '''
     TweetMiner Documentation
    ==========================

    This TweetCrawler is a pet project I built on a lazy 
    afternoon in my civil service. It'll eventually
    be able to do several tasks related to twitter and 
    twitter data, but for now it's a work in progress.

    - Julius Rajala, 2015

     Controls
    ===========================

     Command       : Operation
    ===========================

    gettimeline n : Gets n number of latest items from your timeline.
    status        : Returns the number of API calls you have left on different 
                    tasks.
    stream #word  : Starts a twitter stream, following #word
    exit          : Exit the application
    docs          : Prints this documentation again.

    '''
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
                        "stream":self.getStream,
                        "docs":self.printDocs
                        }
    
    #Prints application documentation
    def printDocs(self,extra):
        print self.__doc__

    #Starts the streaming service
    def getStream(self, extra):
        # enc = codecs.lookup(extra[0].encoding)
        for x in range(len(extra)):
            print extra[x]
            extra[x] = extra[x].decode("cp1252")
            print extra[x].encode("cp1252")

        streamlistener.main(self.auth, extra)

    #Closes the application
    def quit(self, extra):
        self.running = False

    #A working in progress method to check your remaining api calls
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
            print "Commandline: (Write docs for help)" 
            command = raw_input(">> ").lower()
            command = command.split(" ")
            if command[0] in self.controls:
                self.controls[command[0]](command[1:] if len(command) >=2 else "Nothing here")

    #Returns tweets from users timeline
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
    import codecs
    from tweepy import OAuthHandler
    from lib import secrets as s
    import streamlistener
    
    TweetApp().run()