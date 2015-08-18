# -*- encoding: utf-8 -*-

from tweepy import Stream
from tweepy.streaming import StreamListener

class wordListener(StreamListener):
    def on_data(self, data):
        try:
            with open("twit_stream.json", "a") as f:
                f.write(data)
                return True
        except BaseException as e:
            print "Error on_data: %s" %str(e)
        return True

    def on_error(self, error):
        print(status)
        return True

def main(auth, criteria):
    twitterStream = Stream(auth, wordListener())
    twitterStream.filter(track=["#python"])