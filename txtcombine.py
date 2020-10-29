corpus_title = input("Enter the name for this corpus: ")
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