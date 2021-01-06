from __future__ import print_function
import markovify
from collections import Counter
import random
import sys
import kv
sys.path.append('/usr/local/lib/python3.8/site-packages')


def gentext(text):
    sentences = []
    for i in range(9):
        sentences.append(text.make_sentence())
        result = '\n'.join(sentences)
    return(result)

def generate(text):
    print ("\n")
    print(gentext(text))
    print ("\n")
    sentences = [text.make_sentence(tries=1000) for i in range(5)]
    result = '\n'.join(sentences)
    print(result)
    print ("\n")
    return(result)


