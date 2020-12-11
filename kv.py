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

kafka = markovify.Text(open("txt/kafka.txt"))
finnegan = markovify.Text(open("txt/fw.txt"))
shakespeare = markovify.Text(open("txt/shakespeare-macbeth.txt"))
beckett = markovify.Text(open("txt/threenovels.txt"))
wittgenstein = markovify.Text(open("txt/wittgenstein.txt"))
dante = markovify.Text(open("txt/dante.txt"))
wells = markovify.Text(open("txt/wells.txt"))
blake = markovify.Text(open("txt/blake-poems.txt"))
thursday = markovify.Text(open("txt/chesterton-thursday.txt"))
frost = markovify.Text(open("txt/frost.txt"))
whitman = markovify.Text(open("txt/whitman-leaves.txt"))
unknown = markovify.Text(open("txt/unknown.txt"))
dantewellswittgenstein = markovify.Text(open("txt/dante-wells-wittgenstein.txt"))
unknown_shakespeare_witt = markovify.Text(open("txt/unknown_shakespeare_witt.txt"))
wits = markovify.Text(open("txt/wits2.txt"))
parasite = markovify.Text(open("txt/parasite.txt"))
california= markovify.Text(open("txt/california.txt"))
fail= markovify.Text(open("txt/fail.txt"))



# ====== COMBINED MODELS
combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

combo2 = markovify.combine([ beckett, wits, whitman], [ 2, 1, 1 ])

combo3 = markovify.combine([ parasite, california, fail ], [ 1, 1, 1 ])

combo5 = markovify.combine([ kafka, shakespeare, beckett ], [ 1, 1.5, 1 ])

'''
mods = [combo1, combo2, combo3, combo5, kafka,
        finnegan, shakespeare, beckett, wittgenstein,
        dante, wells, blake, thursday, frost, whitman,
        unknown, dantewellswittgenstein,
        unknown_shakespeare_witt, wits, parasite,
        california, fail] 
'''
# loads markov chains from pickle file
with open('models.pkl', 'rb') as f:
    modelDict = pickle.load(f)
keys = list(modelDict)
chains = modelDict.values()
mods = list(chains)



# with open('mods.txt', 'wb') as f:
#     pickle.dump(mods, f)

# TODO run this once, store the mods, and create a load models
# function in k2.py 
# to test in k2.py: for mods in mod: kf.generate(mods[mod])

with open('choices.txt', 'rb') as f:
    models = pickle.load(f)

# with open('txt/mods.txt', 'rb') as f:
#     mods = pickle.load(f)



# when a new model is created, the id will be len(models) - 1
modelID = len(models) - 1
print(modelID)
# it will be inserted at len(models) - 2 before exit options
modelIndex = modelID - 1
print(modelIndex)

# TODO markovify corpus inside newmodel() and insert into mods list

def newmodel():
    '''
    class Mod(object):
        def __init__(self, corpus_title):
            self.corpus_title = corpus_title 
    modDict = {}
    '''
    print(f"This corpus will have an ID of {modelID}")
    corpus_title = input("Enter a name for this corpus: ")
    # modDict[corpus_title] = Mod[corpus_title]
    input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")
    filenames = input_corpus_files.split()
    print(f"filenames are {filenames}")
    with open(f'txt/{corpus_title}.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    newtuple = (corpus_title, modelID)
    print(newtuple)
    models.insert(modelIndex, newtuple)
    mods.append(markovify.NewlineText(open(f'txt/{corpus_title}.txt')))
    with open('txt/mods.txt', 'wb') as f:
        pickle.dump(mods, f)
    with open('choices.txt', 'wb') as f:
        pickle.dump(models, f)
    print("complete")



# models = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('Return to main menu', 'return'), ('Exit', 'exit')]


# models_json = json.dumps(models)

# with open('models.json', 'w') as outfile:
#    json.dump(models_json, outfile)

# with open('choices.json') as json_file:
#    data = json.loads(json_file)
#    models = data['Choices']
