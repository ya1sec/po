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

# Generates list of choices for inquirer.prompt(gq) + inquirer.prompt(dq)
def getChoices():
    # load dict of markov models from pickle file
    with open('models.pkl', 'rb') as f:
        modelDict = pickle.load(f)
    keys = list(modelDict)
    chains = modelDict.values()
    mods = list(chains)
    choiceList = []
    for key in keys:
        choiceList.append(key)
    choiceList.append(('Return to main menu', 'return'))
    choiceList.append(('Exit', 'exit'))
    return choiceList

listLen = len(kv.keys)

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
                  choices=getChoices())
]

answers = inquirer.prompt(q)

while True:
    if answers['action'] == 'gen':
        # print("working")
        genanswers = inquirer.prompt(gq)
        if genanswers['model'] == 'return':
            answers = inquirer.prompt(q)
            continue
        if genanswers['model'] == 'exit':
            break
        for key in kv.keys:
            if genanswers['model'] == key:
                kf.generate(kv.mods[key - 1])
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
                keys.remove(delIndex)
                mods.remove(delIndex)
        print(delID)
        if answer['delete'] == 'return':
            answers = inquirer.prompt(q)
            continue
        if answer['delete'] == 'exit':
            break
    else:
        break
    print(answers)











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
