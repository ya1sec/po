
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




models = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('Return to main menu', 'return'), ('Exit', 'exit')]


models_json = json.dumps(models)

with open('models.json', 'w') as outfile:
   json.dump(models_json, outfile)

with open('choices.json') as json_file:
   data = json.loads(json_file)
   models = data['Choices']

   """
print("\n")
print(generate(combo1))
print("\n")

sentences = [combo1.make_sentence(tries=1000) for i in range(5)]
new_para = '\n'.join(sentences)
print(new_para)
print("\n")

"""


with open('kafka.json') as json_file:
    kafka_json = json.load(json_file)
with open('fin.json') as json_file:
    fin_json = json.load(json_file)
with open('macbeth.json') as json_file:
    macbeth_json = json.load(json_file)
with open('beckett.json') as json_file:
    beckett_json = json.load(json_file)
with open('witt.json') as json_file:
    witt_json = json.load(json_file)
with open('dante.json') as json_file:
    dante_json = json.load(json_file)
with open('wells.json') as json_file:
    wells_json = json.load(json_file)
with open('blake.json') as json_file:
    blake_json = json.load(json_file)
with open('thursday.json') as json_file:
    thursday_json = json.load(json_file)
with open('frost.json') as json_file:
    frost_json = json.load(json_file)
with open('whitman.json') as json_file:
    whitman_json = json.load(json_file)
with open('unknown.json') as json_file:
    unknown_json = json.load(json_file)
with open('wits.json') as json_file:
    wits_json = json.load(json_file)
with open('dantewellswitt.json') as json_file:
    dantewellswitt_json = json.load(json_file)
with open('unknownshakespearewitt.json') as json_file:
    unknownshakespearewitt_json = json.load(json_file)
with open('combo1.json') as json_file:
    combo1_json = json.load(json_file)
with open('combo2.json') as json_file:
    combo2_json = json.load(json_file)


kafka = markovify.Text.from_json(kafka_json)
fin = markovify.Text.from_json(fin_json)
macbeth = markovify.Text.from_json(macbeth_json)
beckett = markovify.Text.from_json(beckett_json)
witt = markovify.Text.from_json(witt_json)
dante = markovify.Text.from_json(dante_json)
wells = markovify.Text.from_json(wells_json)
blake = markovify.Text.from_json(blake_json)
thursday = markovify.Text.from_json(thursday_json)
frost = markovify.Text.from_json(frost_json)
whitman = markovify.Text.from_json(whitman_json)
unknown = markovify.Text.from_json(unknown_json)
dantewellswitt = markovify.Text.from_json(dantewellswitt_json)
unknownshakespearewitt = markovify.Text.from_json(unknownshakespearewitt_json)
combo1 = markovify.Text.from_json(combo1_json)
combo2 = markovify.Text.from_json(combo2_json)

