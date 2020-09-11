from __future__ import print_function
import random
# from shmarkov import *
# import nltk
# from nltk.corpus import gutenberg
from collections import Counter
import markovify


kafka = markovify.Text(open("kafka.txt"))
finnegan = markovify.Text(open("fw.txt"))
shakespeare = markovify.Text(open("shakespeare-macbeth.txt"))
beckett = markovify.Text(open("bonbon.txt"))
wittgenstein = markovify.Text(open("wittgenstein.txt"))
dante = markovify.Text(open("dante.txt"))
wells = markovify.Text(open("wells.txt"))
blake = markovify.Text(open("blake-poems.txt"))
thursday = markovify.Text(open("chesterton-thursday.txt"))
frost = markovify.Text(open("frost.txt"))
whitman = markovify.Text(open("whitman-leaves.txt"))
unknown = markovify.Text(open("unknown.txt"))
will = markovify.Text(open("will.txt"))
edin = markovify.Text(open("edinburgh.txt"))

# ====== COMBINED MODELS
combo1 = markovify.combine([ kafka, finnegan, shakespeare, beckett, wittgenstein, dante, wells ], [ 1.5, 1, 1, 1.5, 1.5, 1, 1 ])

combo2 = markovify.combine([ kafka, finnegan, shakespeare, beckett ], [ 2, 1, 1, 1.5 ])

combo3 = markovify.combine([ dante, wells, wittgenstein], [ 1, 1, 1 ])


combo4 = markovify.combine([ blake, thursday, frost, whitman ], [ 1, 1, 1, 1 ])

combo5 = markovify.combine([ unknown, will, edin ], [ 1, 1, 1 ])

"""
TODO:
* combo2 = kafka, joyce, shakespeare, beckett
* combo3 = dante, wells, wittgenstein

"""

print ("\n")
print("===== KORPIS =====")


def generate(text):
    sentences = []
    for i in range(9):
        sentences.append(combo1.make_sentence())
        result = '\n'.join(sentences)
    return(result)


print(generate(combo1))
print ("\n")

sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
new_para = '\n'.join(sentences)
print(new_para)

#NOTE combo 2

print ("\n")
print("===== KAFKA, JOYCE, SHAKESPEARE, BECKETT =====")


def generate(text):
    sentences = []
    for i in range(9):
        sentences.append(combo2.make_sentence())
        result = '\n'.join(sentences)
    return(result)


print(generate(combo2))

print ("\n")
print("===== DANTE, WELLS, WITTGENSTEIN =====")

for i in range(9):
    print(combo3.make_sentence())

print ("\n")


print("===== #$# =====")

for i in range(9):
    print(combo4.make_sentence())

print ("\n")



print ("\n")


print("===== another =====")

for i in range(9):
    print(combo4.make_sentence())

print ("\n")



# print("===================================================================================\n")


# sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
# new_para = '\n'.join(sentences)
# print(new_para)

# print ("\n")
# print("===================================================================================\n")




# with open("fw.txt") as f:
#     text = f.read()

# text_model = markovify.Text(text)

# for i in range(5):
#     print(text_model.make_sentence())

# # Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))

# gutenberg.fileids()

# macbeth = tuple(gutenberg.words("shakespeare-macbeth.txt"))

# print(macbeth)

# text = open(gutenberg.raw("shakespeare-macbeth.txt")).read()

# words = text.split()

# for item in markov_generate_from_lines_in_file(10, open("fw.txt"), 20, 'char'):
#     print(item)

# inputModel = markov_model(3, "she sells seashells by the seashore")
# for i in range(12):
#     print(''.join(gen_from_model(3, inputModel)))
# print(words)

# pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]

# pairs = []
# for i in range(len(words)-1):
#     this_pair = (words[i], words[i+1])
#     pairs.append(this_pair)


# pair_counts = Counter(pairs)
# print(pair_counts.most_common(10))
