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


with open('choices.txt', 'rb') as f:
    models = pickle.load(f)

# with open('txt/mods.txt', 'rb') as f:
#     mods = pickle.load(f)

# when a new model is created, the id will be len(models) - 1
# modelID = len(models) - 1
modelID = len(keys) + 1
# print(modelID)
# it will be inserted at len(models) - 2 before exit options
modelIndex = modelID - 1
#print(modelIndex)



def newmodel():
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
    # insert tuple into choices list
    models.insert(modelIndex, newtuple)
    newModel = markovify.NewlineText(open(f'txt/{corpus_title}.txt'))
    # Insert Dict with corpus title and model into modelDict
    newDict = {modelID: newModel}
    modelDict.update(newDict)
    with open('mods.pkl', 'wb') as f:
        pickle.dump(modelDict, f)
    with open('choices.txt', 'wb') as f:
        pickle.dump(models, f)
    print("complete")



# models = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('Return to main menu', 'return'), ('Exit', 'exit')]
