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

kafka = markovify.NewlineText(open("txt/kafka.txt"))
finnegan = markovify.NewlineText(open("txt/fw.txt"))
shakespeare = markovify.NewlineText(open("txt/shakespeare-macbeth.txt"))
beckett = markovify.NewlineText(open("txt/threenovels.txt"))
wittgenstein = markovify.NewlineText(open("txt/wittgenstein.txt"))
dante = markovify.NewlineText(open("txt/dante.txt"))
wells = markovify.NewlineText(open("txt/wells.txt"))
blake = markovify.NewlineText(open("txt/blake-poems.txt"))
thursday = markovify.NewlineText(open("txt/chesterton-thursday.txt"))
frost = markovify.NewlineText(open("txt/frost.txt"))
whitman = markovify.NewlineText(open("txt/whitman-leaves.txt"))
unknown = markovify.NewlineText(open("txt/unknown.txt"))
dantewellswittgenstein = markovify.NewlineText(open("txt/dante-wells-wittgenstein.txt"))
unknown_shakespeare_witt = markovify.NewlineText(open("txt/unknown_shakespeare_witt.txt"))
wits = markovify.NewlineText(open("txt/wits2.txt"))
parasite = markovify.NewlineText(open("txt/parasite.txt"))
california= markovify.NewlineText(open("txt/california.txt"))
fail= markovify.NewlineText(open("txt/fail.txt"))

 # ====== COMBINED MODELS
combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

combo2 = markovify.combine([ beckett, wits, whitman], [ 2, 1, 1 ])

combo3 = markovify.combine([ parasite, california, fail ], [ 1, 1, 1 ])

combo5 = markovify.combine([ kafka, shakespeare, beckett ], [ 1, 1.5, 1 ])

mods = [combo1, combo2, combo3, combo5, kafka,
        finnegan, shakespeare, beckett, wittgenstein,
        dante, wells, blake, thursday, frost, whitman,
        unknown, dantewellswittgenstein,
        unknown_shakespeare_witt, wits, parasite,
        california, fail]

dict = {};

for mod in mods:
    i = mods.index(mod) + 1
    newDict = {i: mod}
    dict.update(newDict)
    print(i)
print("worked")


# jsonDict = json.dumps(dict)

f = open('models.pkl', 'wb')
pickle.dump(dict, f)
f.close()
print('pickled')

# for j in jsonList:
#     with open(f'modjson.txt', 'w') as outfile:
#         json.dump(modjson, outfile)
#     print("done")
# print("complete") 