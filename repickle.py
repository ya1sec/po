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

with open('choices.txt', 'rb') as f:
    models = pickle.load(f)

models.remove(model)