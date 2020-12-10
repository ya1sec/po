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

models = kv.models

# def deleteMod(mod):
#     with open('choices.')














"""
print("\n")
print(generate(combo1))
print("\n")

sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
new_para = '\n'.join(sentences)
print(new_para)
print("\n")

"""

"""

with open('kafka.json') as json_file:
    kafka_json = json.load(json_file)
with open('fin.json') as json_file:
    fin_json = json.load(json_file)
with open('macbeth.json') as json_file:
    macbeth_json = json.load(json_file)
with open('beckett.json') as json_file:
    beckett_json = json.load(json_file)
with open('witt.json') as json_file:
    witt_json = json.load(json_file)
with open('dante.json') as json_file:
    dante_json = json.load(json_file)
with open('wells.json') as json_file:
    wells_json = json.load(json_file)
with open('blake.json') as json_file:
    blake_json = json.load(json_file)
with open('thursday.json') as json_file:
    thursday_json = json.load(json_file)
with open('frost.json') as json_file:
    frost_json = json.load(json_file)
with open('whitman.json') as json_file:
    whitman_json = json.load(json_file)
with open('unknown.json') as json_file:
    unknown_json = json.load(json_file)
with open('wits.json') as json_file:
    wits_json = json.load(json_file)
with open('dantewellswitt.json') as json_file:
    dantewellswitt_json = json.load(json_file)
with open('unknownshakespearewitt.json') as json_file:
    unknownshakespearewitt_json = json.load(json_file)
with open('combo1.json') as json_file:
    combo1_json = json.load(json_file)
with open('combo2.json') as json_file:
    combo2_json = json.load(json_file)


kafka = markovify.Text.from_json(kafka_json)
fin = markovify.Text.from_json(fin_json)
macbeth = markovify.Text.from_json(macbeth_json)
beckett = markovify.Text.from_json(beckett_json)
witt = markovify.Text.from_json(witt_json)
dante = markovify.Text.from_json(dante_json)
wells = markovify.Text.from_json(wells_json)
blake = markovify.Text.from_json(blake_json)
thursday = markovify.Text.from_json(thursday_json)
frost = markovify.Text.from_json(frost_json)
whitman = markovify.Text.from_json(whitman_json)
unknown = markovify.Text.from_json(unknown_json)
dantewellswitt = markovify.Text.from_json(dantewellswitt_json)
unknownshakespearewitt = markovify.Text.from_json(unknownshakespearewitt_json)
combo1 = markovify.Text.from_json(combo1_json)
combo2 = markovify.Text.from_json(combo2_json)

"""
