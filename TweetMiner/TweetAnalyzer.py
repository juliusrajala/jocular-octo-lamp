# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re

global emoticonStr
global regexStr

emoticonStr = r"""
        (?:
        [:=;] #eyes
        [oO\-]? #nose
        [D\)\]\(\]/\\OpP] #mouth
        )"""

regexStr = [
    emoticonStr,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokensRe = re.compile(r'('+''.join(regexStr)+')', re.VERBOSE | re.IGNORECASE)
emoticonRe = re.compile(r'^'+emoticonStr+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokensRe.findall(s)

def preprocess(s, lowercase = False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticonRe.search(token) else token.lower() for token in tokens]
    return tokens

tweet = "RT @marcobonzanini: just an example! :D http://example.com #NLP"
print preprocess(tweet)