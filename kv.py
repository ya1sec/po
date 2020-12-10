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



# ====== COMBINED MODELS
combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

combo2 = markovify.combine([ beckett, wits, whitman], [ 2, 1, 1 ])

combo3 = markovify.combine([ parasite, california, fail ], [ 1, 1, 1 ])

combo5 = markovify.combine([ kafka, shakespeare, beckett ], [ 1, 1.5, 1 ])


# models = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('Return to main menu', 'return'), ('Exit', 'exit')]


# models_json = json.dumps(models)

# with open('models.json', 'w') as outfile:
#    json.dump(models_json, outfile)



with open('choices.txt', 'rb') as f:
    models = pickle.load(f)

# with open('choices.json') as json_file:
#    data = json.loads(json_file)
#    models = data['Choices']

# when a new model is created, the id will be len(models) - 1
modelID = len(models) - 1
print(modelID)
# it will be inserted at len(models) - 2 before exit options
modelIndex = modelID - 1
print(modelIndex)


def newmodel():
    print(f"This corpus will have an ID of {modelID}")
    corpus_title = input("Enter a name for this corpus: ")
    input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")
    filenames = input_corpus_files.split()
    print(f"filenames are {filenames}")
    with open(f'{corpus_title}.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    newtuple = (corpus_title, modelID)
    print(newtuple)
    models.insert(modelIndex, newtuple)
    with open('choices.txt', 'wb') as f:
        pickle.dump(models, f)
    print("complete")
