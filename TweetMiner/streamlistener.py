# -*- encoding: cp1252 -*-

import msvcrt as m
import thread
from tweepy import Stream
from tweepy.streaming import StreamListener

#Class wordlistener extends streamlistener is used to follow the stream
class wordListener(StreamListener):
    def __init__(self, criteria):
        self.hashtag = ""
        for x in range(0,len(criteria)):
            self.hashtag += criteria[x]+"_"
        self.hashtag.replace("#", "")
        self.hashtag = self.hashtag[:-1]
        self.hashtag = self.hashtag.encode("cp1252")
        print self.hashtag
        self.keyPressed = False
        self.tweets = 0

    #Catches tweets and writes them to an according file
    def on_data(self, data):
        while not self.keyPressed:
            try:
                self.tweets+=1
                print "Tweet caught: " + data
                self.write_json(data)
                return True
            except BaseException as e:
                print "Error on_data: %s" %str(e)
            return True

    #Catches errors and returns the error message.
    def on_error(self, error):
        while not self.keyPressed:
            print(error)
            return True

    def write_json(self, data):

        with open("json/" + self.hashtag + ".json", "a") as f:
                    f.write(data)

    #Catches stream disconnection and returns the notice
    def on_disconnect(self, notice):
        print "Disconnected: "+ notice

def quit():
    global running 
    print "Closing down the stream"
    running = False

def wait():
    m.getch()
    if m.getch == "a":
        quit()

def main(auth, criteria):
    global running
    running = True
    print criteria
    # for x in range(len(criteria)):
    #     criteria[x] = criteria[x].encode("cp1252")
    print "Encoded: " + criteria[0].encode("cp1252")
    # criteria = criteria[0]# if str(criteria[0])[0] == "#" else "#"+criteria[0]
    thread.start_new_thread(wait, ())
    while running:
        try:
            print "Initializing listener and starting stream"
            listener = wordListener(criteria[0:])
            print "ctrl + c to disconnect"
            
            twitterStream = Stream(auth, listener)
            twitterStream.filter(track=criteria)
        except KeyboardInterrupt:
            print "Caught keyboard interruption."
            twitterStream.disconnect()
            break
