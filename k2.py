from __future__ import print_function
import sys
import kf
import kv
import choices
sys.path.append('/usr/local/lib/python3.8/site-packages')
import random
from collections import Counter
import markovify
import inquirer
from termcolor import colored, cprint


"""
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


text = colored('WELCOME TO KORPIS', 'white', attrs=['reverse', 'blink'])
print(text)

models = [('1', '1'), ('2','2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('Return to main menu', 'return'), ('Exit', 'exit')]

# when a new model is created, the id will be len(models) - 1
modelID = len(models) - 1
print(modelID)
# it will be inserted at len(models) - 2 before exit options
modelIndex = modelID - 1
print(modelIndex)


"""

text = colored('WELCOME TO KORPIS', 'white', attrs=['reverse', 'blink'])
print(text)

q = [
    inquirer.List('action',
                  message="What would you like to do?",
                  choices=[('Generate from model', 'gen'), ('Make new model', 'new'), ('Exit', 'exit')])
]

gq = [
    inquirer.List('model',
                  message="Choose a model to generate from:",
                  choices=choices.models)
]

answers = inquirer.prompt(q)
while True:

    print(len(kv.models)) 

    if answers['action'] == 'gen':
        # print("working")
        genanswers = inquirer.prompt(gq)
        if genanswers['model'] == 1: 
            kf.gen2(kv.combo2)
            continue
        if genanswers['model'] == 2:
            kf.gen2(kv.combo1)
            continue
        if genanswers['model'] == 3:
            kf.gen2(kv.combo3)
            continue
        if genanswers['model'] == 4:
            kf.gen2(kv.unknown_shakespeare_witt)
            continue
        if genanswers['model'] == 5:
            kf.gen2(kv.combo5)
            continue
        if genanswers['model'] == 6:
            kf.gen2(kv.beckett)
            continue
        if genanswers['model'] == 'return':
            answers = inquirer.prompt(q)
            continue

    if answers['action'] == 'new':
        kv.newmodel()
        answers = inquirer.prompt(q)
        continue
    else:
        break
    print(answers)

"""
        corpus_title = input("Enter a name for this corpus: ")
        input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")


        filenames = input_corpus_files.split()
        print(f"filenames are {filenames}")



        # filenames = ['./data/shakespeare-macbeth.txt', "./data/fw.txt"]
        with open(f'{corpus_title}.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        print("complete")
        answers = inquirer.prompt(q)
        continue

    else:
        break

    print(answers)


# ================================================================================
"""


"""
    if answers['action'] == 'new':
        print(f"This corpus will have an ID of {modelID}")
        corpus_title = input("Enter a name for this corpus: ")
        input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")


        filenames = input_corpus_files.split()
        print(f"filenames are {filenames}")
        
        

        # filenames = ['./data/shakespeare-macbeth.txt', "./data/fw.txt"]
        with open(f'{corpus_title}.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        print("complete")
        answers = inquirer.prompt(q)
        continue

    else:
        break

    print(answers)

def newmodel():

    print(f"This corpus will have an ID of {modelID}")
    corpus_title = input("Enter a name for this corpus: ")
    input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")


    filenames = input_corpus_files.split()
    print(f"filenames are {filenames}")
    
    

    # filenames = ['./data/shakespeare-macbeth.txt', "./data/fw.txt"]
    with open(f'{corpus_title}.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    print("complete")
"""
