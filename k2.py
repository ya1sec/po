from __future__ import print_function
import sys
import kf
import kv
import choices
import pickle
sys.path.append('/usr/local/lib/python3.8/site-packages')
import random
from collections import Counter
import markovify
import inquirer
from termcolor import colored, cprint


text = colored('WELCOME TO KORPIS', 'white', attrs=['reverse', 'blink'])
print(text)

# with open('choices.txt', 'rb') as f:
#    models = pickle.load(f)

# models = kv.models

listLen = len(kv.models)
modelID = kv.modelID
modelIndex = kv.modelIndex
print(f"the value of model {kv.models[6][0]} one is {kv.models[0][1]}")

lastly = [('Return to main menu', 'return'), ('Exit', 'exit')]

# kv.modelDict.update(('Return to main menu', 'return'))

# def getChoices():
#     insertAt = len(kv.keys) - 2
#     for key in kv.keys:
#         i = kv.keys.index(key) + 1
#         tup = (key, i)
#         choiceList.insert(insertAt, tup)
#     # return choiceList
def getChoices():
    choiceList = []
    for key in kv.keys:
        choiceList.append(key)
    choiceList.append(('Return to main menu', 'return'))
    choiceList.append(('Exit', 'exit'))
    return choiceList

q = [
    inquirer.List('action',
                  message="What would you like to do?",
                  choices=[('Generate from model', 'gen'), ('Make new model', 'new'), ('Delete a model', 'delete'), ('Exit', 'exit')])
]

gq = [
    inquirer.List('model',
                  message="Choose a model to generate from:",
                  choices=getChoices())
]

dq = [
    inquirer.List('delete',
                  message="Choose a model to delete:",
                  choices=kv.models)
]

answers = inquirer.prompt(q)

while True:
    if answers['action'] == 'gen':
        # print("working")
        genanswers = inquirer.prompt(gq)
        # if genanswers['model'] == 1: 
        #     kf.generate(kv.mods[1])
        #     continue
        # if genanswers['model'] == 2:
        #     kf.generate(kv.mods[0])
        #     continue
        # if genanswers['model'] == 3:
        #     kf.generate(kv.mods[4])
        #     continue
        # if genanswers['model'] == 4:
        #     kf.generate(kv.mods[18])
        #     continue
        # if genanswers['model'] == 5:
        #     kf.generate(kv.mods[3])
        #     continue
        # if genanswers['model'] == 6:
        #     kf.generate(kv.mods[7])
        #     continue

        if genanswers['model'] == 'return':
            answers = inquirer.prompt(q)
            continue
        if genanswers['model'] == 'exit':
            break
        for key in kv.keys:
            if genanswers['model'] == key:
                kf.generate(kv.mods[key])
                continue
        continue
    if answers['action'] == 'new':
        kv.newmodel()
        answers = inquirer.prompt(q)
        continue
    if answers['action'] == 'delete':
        answer = inquirer.prompt(dq)
        delID = answer['delete']
        if isinstance(delID, int):
            if delID < listLen - 2:
                delIndex = delID - 1
                kv.models.remove(delIndex)
        print(delID)
        if answer['delete'] == 'return':
            answers = inquirer.prompt(q)
            continue
        if answer['delete'] == 'exit':
            break
    else:
        break
    print(answers)

