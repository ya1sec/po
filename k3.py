from __future__ import print_function
import markovify
import json
from collections import Counter
import random
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')


# with open('kafka.json') as json_file:
#     kafka_json = json.load(json_file)

# kafka = markovify.Text.from_json(kafka_json)


# for i in range(9):
#     print(kafka.make_sentence())
# print("\n")

kafka = markovify.Text(open("kafka.txt").read())
finnegan = markovify.Text(open("fw.txt").read())
shakespeare = markovify.Text(open("shakespeare-macbeth.txt").read())
beckett = markovify.Text(open("threenovels.txt").read())
wittgenstein = markovify.Text(open("wittgenstein.txt").read())
dante = markovify.Text(open("dante.txt").read())
wells = markovify.Text(open("wells.txt").read())
blake = markovify.Text(open("blake-poems.txt").read())
thursday = markovify.Text(open("chesterton-thursday.txt").read())
frost = markovify.Text(open("frost.txt").read())
whitman = markovify.Text(open("whitman-leaves.txt").read())
unknown = markovify.Text(open("unknown.txt").read())
will = markovify.Text(open("will.txt").read())
edin = markovify.Text(open("edinburgh.txt").read())
dantewellswittgenstein = markovify.Text(open("dante-wells-wittgenstein.txt").read())
unknown_shakespeare_witt = markovify.Text(open("unknown_shakespeare_witt.txt").read())
wits = markovify.Text(open("wits2.txt").read())


# ====== COMBINED MODELS
combo1 = markovify.combine([kafka, finnegan, shakespeare, beckett,
                            wittgenstein, dante, wells], [1.5, 1, 1, 1.5, 1.5, 1, 1])

combo2 = markovify.combine([kafka, shakespeare, beckett], [1, 1.5, 1])

combo1 = combo1.compile()
combo2 = combo2.compile()

combo1_json = combo1.to_json()
combo2_json = combo2.to_json()
kafka_json = kafka.to_json()
fin_json = finnegan.to_json()
macbeth_json = shakespeare.to_json()
beckett_json = beckett.to_json()
witt_json = wittgenstein.to_json()
dante_json = dante.to_json()
wells_json = wells.to_json()
blake_json = blake.to_json()
thursday_json = thursday.to_json()
frost_json = frost.to_json()
whitman_json = whitman.to_json()
unknown_json = unknown.to_json()
dantewellswitt_json = dantewellswittgenstein.to_json()
unknownshakespearewitt_json = unknown_shakespeare_witt.to_json()
wits_json = wits.to_json()


with open('combo1.json', 'w') as outfile:
    json.dump(combo1_json, outfile)
print("complete")
with open('combo2.json', 'w') as outfile:
    json.dump(combo2_json, outfile)
print("complete")
with open('fin.json', 'w') as outfile:
    json.dump(fin_json, outfile)
print("complete")
with open('macbeth.json', 'w') as outfile:
    json.dump(macbeth_json, outfile)
print("complete")
with open('beckett.json', 'w') as outfile:
    json.dump(beckett_json, outfile)
print("complete")
with open('witt.json', 'w') as outfile:
    json.dump(witt_json, outfile)
print("complete")
with open('dante.json', 'w') as outfile:
    json.dump(dante_json, outfile)
print("complete")
with open('wells.json', 'w') as outfile:
    json.dump(wells_json, outfile)
print("complete")
with open('blake.json', 'w') as outfile:
    json.dump(blake_json, outfile)
print("complete")
with open('thursday.json', 'w') as outfile:
    json.dump(thursday_json, outfile)
print("complete")
with open('frost.json', 'w') as outfile:
    json.dump(frost_json, outfile)
print("complete")
with open('whitman.json', 'w') as outfile:
    json.dump(whitman_json, outfile)
print("complete")
with open('unknown.json', 'w') as outfile:
    json.dump(unknown_json, outfile)
print("complete")
with open('dantewellswitt.json', 'w') as outfile:
    json.dump(dantewellswitt_json, outfile)
print("complete")
with open('unknownshakespearewitt.json', 'w') as outfile:
    json.dump(unknownshakespearewitt_json, outfile)
print("complete")
with open('wits.json', 'w') as outfile:
    json.dump(wits_json, outfile)
print("complete")


# ====== COMBINED MODELS
# combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

# combo2 = markovify.combine([ kafka, shakespeare, beckett ], [ 1, 1.5, 1 ])

# combo3 = markovify.combine([ dante, wells, wittgenstein], [ 1, 1, 1 ])


# combo4 = markovify.combine([ blake, thursday, frost, whitman ], [ 1, 1, 1, 1 ])

# combo5 = markovify.combine([ unknown, will, edin ], [ 1, 1, 1 ])

# combo6 = markovify.combine([ unknown, will, edin ], [ 1, 1, 1 ])

# text = colored('WELCOME TO KORPIS', 'white', attrs=['reverse', 'blink'])
# print(text)


# q = [
#     inquirer.List('action',
#                   message="What would you like to do?",
#                   choices=[('Generate from model', 'gen'), ('Make new model', 'new'), ('Exit', 'exit')])
# ]

# gq = [
#     inquirer.List('model',
#                   message="Choose a model to generate from:",
#                   choices=[('full-corpis', '1'), ('kafka-joyce-shakespeare-beckett',
#                       '2'), ('dante-wells-wittgenstein', '3'), ('unknown', '4'),
#                       ('shakespeare', '5'), ('beckett', '6'), ('Return to main menu', 'return'), ('Exit', 'exit')])
# ]

# answers = inquirer.prompt(q)
# while True:

#     if answers['action'] == 'gen':
#         # print("working")
#         genanswers = inquirer.prompt(gq)
#         if genanswers['model'] == '1':
#             def generate(text):
#                 sentences = []
#                 for i in range(9):
#                     sentences.append(combo1.make_sentence())
#                     result = '\n'.join(sentences)
#                 return(result)
#             print ("\n")
#             print(generate(combo1))
#             print ("\n")

#             sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
#             new_para = '\n'.join(sentences)
#             print(new_para)
#             print ("\n")
#             continue
#         if genanswers['model'] == '2':
#             def generate(text):
#                 sentences = []
#                 for i in range(9):
#                     sentences.append(combo2.make_sentence())
#                     result = '\n'.join(sentences)
#                 return(result)
#             print ("\n")
#             print(generate(combo2))
#             print ("\n")
#             continue
#         if genanswers['model'] == '3':
#             print("\n")
#             for i in range(9):
#                 print(dantewellswittgenstein.make_sentence())
#             print("\n")
#             continue
#         if genanswers['model'] == '4':
#             print("\n")
#             for i in range(9):
#                 print(unknown_shakespeare_witt.make_sentence())
#             print("\n")
#             continue
#         if genanswers['model'] == '5':
#             print("\n")
#             for i in range(9):
#                 print(shakey.make_sentence())
#             print("\n")
#             continue
#         if genanswers['model'] == '6':
#             print("\n")
#             for i in range(9):
#                 print(beckett.make_sentence())
#             print("\n")
#             continue
#         if genanswers['model'] == 'return':
#             answers = inquirer.prompt(q)
#             continue

#     if answers['action'] == 'new':
#         corpus_title = input("Enter a name for this corpus: ")
#         input_corpus_files = input("Enter the filenames of each text to be added to this corpus separated by space: ")


#         filenames = input_corpus_files.split()
#         print(f"filenames are {filenames}")


#         # filenames = ['./data/shakespeare-macbeth.txt', "./data/fw.txt"]
#         with open(f'{corpus_title}.txt', 'w') as outfile:
#             for fname in filenames:
#                 with open(fname) as infile:
#                     for line in infile:
#                         outfile.write(line)
#         print("complete")
#         answers = inquirer.prompt(q)
#         continue

#     else:
#         break

#     print(answers)


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
