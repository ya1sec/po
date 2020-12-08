from __future__ import print_function
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
import random
from collections import Counter
import markovify
import inquirer
from termcolor import colored, cprint

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

# ====== COMBINED MODELS
combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

combo2 = markovify.combine([ beckett, wits, whitman], [ 1, 1, 1 ])

combo3 = markovify.combine([ dante, wells, wittgenstein], [ 1, 1, 1 ])

combo5 = markovify.combine([ kafka, shakespeare, beckett ], [ 1, 1.5, 1 ])


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
                  choices=[('1', '1'), ('2',
                      '2'), ('3', '3'), ('4', '4'),
                      ('5', '5'), ('6', '6'), ('Return to main menu', 'return'), ('Exit', 'exit')])
]

answers = inquirer.prompt(q)
while True:

    if answers['action'] == 'gen':
        # print("working")
        genanswers = inquirer.prompt(gq)
        if genanswers['model'] == '1':
            def generate(text):
                sentences = []
                for i in range(9):
                    sentences.append(combo1.make_sentence())
                    result = '\n'.join(sentences)
                return(result)
            print ("\n")
            print(generate(combo1))
            print ("\n")

            sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
            new_para = '\n'.join(sentences)
            print(new_para)
            print ("\n")
            continue
        if genanswers['model'] == '2':
            def generate(text):
                sentences = []
                for i in range(9):
                    sentences.append(combo2.make_sentence())
                    result = '\n'.join(sentences)
                return(result)
            print ("\n")
            print(generate(combo2))
            print ("\n")
            continue
        if genanswers['model'] == '3':
            print("\n")
            for i in range(9):
                print(dantewellswittgenstein.make_sentence())
            print("\n")
            continue
        if genanswers['model'] == '4':
            print("\n")
            for i in range(9):
                print(unknown_shakespeare_witt.make_sentence())
            print("\n")
            continue
        if genanswers['model'] == '5':
            print("\n")
            for i in range(9):
                print(combo5.make_sentence())
            print("\n")
            continue
        if genanswers['model'] == '6':
            print("\n")
            for i in range(9):
                print(beckett.make_sentence())
            print("\n")
            continue
        if genanswers['model'] == 'return':
            answers = inquirer.prompt(q)
            continue

    if answers['action'] == 'new':
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




# options = {}
# #     [USER OPTION] = PROGRAM RESULT
# options['Generate from model'] = 'gen'
# options['Make new model'] = 'new'
# options['Exit'] = 'exit'


# models = {}
# #     [USER OPTION] = PROGRAM RESULT
# models['full-corpis'] = 'all'
# models['kafka-joyce-shakespeare-beckett'] = 'mod1'
# models['dante-wells-wittgenstein'] = 'mod2'
# models['#$#'] = 'mod3'
# models['Exit'] = 'exit'



# def selectFromDict(options, name):

#     index = 0
#     indexValidList = []
#     cprint('Select ' + name + ':', 'cyan')
#     for optionName in options:
#         index = index + 1
#         indexValidList.extend([options[optionName]])
#         indStr = colored(str(index), 'red')
#         cprint(indStr + '. ' + optionName)
#     inputValid = False
#     while not inputValid:
#         inputRaw = input(name + ': ')
#         inputNo = int(inputRaw) - 1
#         if inputNo > -1 and inputNo < len(indexValidList):
#             selected = indexValidList[inputNo]
#             # print('Selected ' +  name + ': ' + selected)
#             inputValid = True
#             # break
#             continue
#         else:
#             print('Please select a valid ' + name + ' number')

#     return selected

# action = selectFromDict(options, 'action')
# # print(action)

# if action == 'gen':
#     modelgen = selectFromDict(models, 'model')
#     if modelgen == 'all':
#         def generate(text):
#             sentences = []
#             for i in range(9):
#                 sentences.append(combo1.make_sentence())
#                 result = '\n'.join(sentences)
#             return(result)
#         print ("\n")
#         print(generate(combo1))
#         print ("\n")

#         sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
#         new_para = '\n'.join(sentences)
#         print(new_para)
#         print ("\n")

#     if modelgen == 'mod1':
#         def generate(text):
#             sentences = []
#             for i in range(9):
#                 sentences.append(combo2.make_sentence())
#                 result = '\n'.join(sentences)
#             return(result)
#         print ("\n")
#         print(generate(combo2))
#         print ("\n")

#     if modelgen == 'mod2':
#         print("\n")
#         for i in range(9):
#             print(dantewellswittgenstein.make_sentence())
#         print("\n")

#     if modelgen == 'mod3':
#         print("\n")
#         for i in range(9):
#             print(unknown_shakespeare_witt.make_sentence())
#         print("\n")




    # print(modelgen)
# elif action == 'new':
#     # call make_corpus()
#     corpus_title = input("Choose a name for this corpus: ")
#     corpus_nickname input("Enter a nickname for this corpus: ")
#     input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")


#     filenames = input_corpus_files.split()
#     print(f"filenames are {filenames}")



#     # filenames = ['./data/shakespeare-macbeth.txt', "./data/fw.txt"]
#     with open(f'{corpus_title}.txt', 'w') as outfile:
#         for fname in filenames:
#             with open(fname) as infile:
#                 for line in infile:
#                     outfile.write(line)

#     # add to list of corpora
#     print("complete")
# elif action == 'exit':
#     break

