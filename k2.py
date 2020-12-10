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


q = [
    inquirer.List('action',
                  message="What would you like to do?",
                  choices=[('Generate from model', 'gen'), ('Make new model', 'new'), ('Delete a model', 'delete'), ('Exit', 'exit')])
]

gq = [
    inquirer.List('model',
                  message="Choose a model to generate from:",
                  choices=kv.models)
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
        if genanswers['model'] == 1: 
            kf.generate(kv.combo2)
            continue
        if genanswers['model'] == 2:
            kf.generate(kv.combo1)
            continue
        if genanswers['model'] == 3:
            kf.generate(kv.combo3)
            continue
        if genanswers['model'] == 4:
            kf.generate(kv.unknown_shakespeare_witt)
            continue
        if genanswers['model'] == 5:
            kf.generate(kv.combo5)
            continue
        if genanswers['model'] == 6:
            kf.generate(kv.beckett)
            continue
        if genanswers['model'] == 'return':
            answers = inquirer.prompt(q)
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

