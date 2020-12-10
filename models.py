from __future__ import print_function
import sys
import kf
import json
import pickle
import choices
sys.path.append('/usr/local/lib/python3.8/site-packages')
import random
from collections import Counter
import markovify



kafka = markovify.Text(open("kafka.txt"))
finnegan = markovify.Text(open("fw.txt"))
shakespeare = markovify.Text(open("shakespeare-macbeth.txt"))
beckett = markovify.Text(open("threenovels.txt"))
wittgenstein = markovify.Text(open("wittgenstein.txt"))
dante = markovify.Text(open("dante.txt"))
wells = markovify.Text(open("wells.txt"))
blake = markovify.Text(open("blake-poems.txt"))
thursday = markovify.Text(open("chesterton-thursday.txt"))
frost = markovify.Text(open("frost.txt"))
whitman = markovify.Text(open("whitman-leaves.txt"))
unknown = markovify.Text(open("unknown.txt"))
dantewellswittgenstein = markovify.Text(open("dante-wells-wittgenstein.txt"))
unknown_shakespeare_witt = markovify.Text(open("unknown_shakespeare_witt.txt"))
wits = markovify.Text(open("wits2.txt"))
parasite = markovify.Text(open("parasite.txt"))
california= markovify.Text(open("california.txt"))
fail= markovify.Text(open("fail.txt"))