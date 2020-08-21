from __future__ import print_function
import random
from shmarkov import *
import nltk
from nltk.corpus import gutenberg
from collections import Counter
import markovify


model_a = markovify.Text(open("whitman-leaves.txt"))
model_b = markovify.Text(open("fw.txt"))
model_c = markovify.Text(open("shakespeare-macbeth.txt"))
model_d = markovify.Text(open("bonbon.txt"))



combo = markovify.combine([ model_a, model_b, model_c, model_d ], [ 1.5, 1, 1, 1.5 ])
print("===================================================================================\n")


def generate(text):
    sentences = []
    for i in range(9):
        sentences.append(combo.make_sentence())
        result = '\n'.join(sentences)
    return(result)


print(generate(combo))

print ("\n")
print("===================================================================================\n")



for i in range(9):
    print(combo.make_sentence())

print ("\n")
print("===================================================================================\n")


sentences = [combo.make_sentence(tries=1000) for i in range(5)]
new_para = '\n'.join(sentences)
print(new_para)

print ("\n")
print("===================================================================================\n")




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
