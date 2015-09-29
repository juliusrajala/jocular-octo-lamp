#-*- coding: utf-8 -*-
import json
import csv

class parser:
    """
    A parser crafted to modify tweets gathered by Hakku
    
                    Hakku @2015 
    Pyry Vanamo, Konsta Sinisalo, Julius Rajala
    """

    def __init__(self,write_location=None, file_location=None):
        if file_location == None:
            print "No file location."
            #Block for testing
            #ShutDown block
        else:
            self.file_location = file_location
            self.write_location = write_location
            self.json_text = []

    def write_to_file(self):
        #Block to write text into csv
        with open(self.write_location + ".csv", "a") as f:
            out = csv.writer(f)
            for line in self.json_text:
                print line
                out.writerow([line])
        f.close()


    def write_tweets(self):
        for line in open(self.file_location):
            try:
                content = json.loads(line)
                content = content['text'].encode('utf-8')
                if len(content) > 5:
                    self.json_text.append(content)
                else:
                    print "Content too short to log"
            except:
                print "Error loading JSON line"

    def run(self):
        #Run block
        print "Reading tweets "
        self.write_tweets()
        self.write_to_file()



if __name__ == '__main__':
    p = parser("json/parsedahmed", "json/istandwithahmed.json")
    p.run()