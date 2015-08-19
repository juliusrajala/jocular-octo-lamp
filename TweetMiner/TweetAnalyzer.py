# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize

global emoticonsStr
global regexStr

emoticonStr = r"""
        (?:
        [:=;] #eyes
        [oO\-]? #nose
        [D\)\]\(\]/\\OpP] #mouth
        )"""

regexStr = [
    emoticonsStr,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokensRe = re.compile