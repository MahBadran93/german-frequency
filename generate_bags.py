from ibag import *
from utility import *
import grammar
import re
#####Load Data

%timeit
fm = "./data/DE_morph_dict.txt"
tfm = "./data/DE_morph_testing.txt"
d = Words()
HEAD_WORD = None
important_parts = {
        "V" ,
    "ADJ",
    "ADV",
    "NN" } 

with open(fm, 'r') as f:
    isIch = True
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = re.split('\W+', line)
        word = words[0]
        if word not in d:
#            if 'ich' in d:
#                if d['ich'][0] in d.Bags.set and isIch:
#                    print("WE FOUND ICH")
#                    isIch = False
#                if d['ich'][0] not in d.Bags.set and not isIch:
#                    print("WE lost ich")
#                    print("At word : " , word)
#                    isIch = True
            d.add_empty(word)
        if len(words) == 1:
            HEAD_WORD = word
        if len(words) > 1:
            if words[1] in important_parts:
                d.set_speach_part(HEAD_WORD)
            d.combine_bags(HEAD_WORD, word)
        counter += 1


### Load FREQUENCY  ###

frequency_file = "./data/de_full_opensubtitle.txt"
not_found_file = "./data/not_found_words.txt"
d.load_frequencies(frequency_file, not_found_file)


### Test ###
import parsing
pars = parsing.Parser(d)

pars.parse("./data/text.txt", "./data/test.txt")



#top 5000 words
with open("./data/5000.txt", 'w') as f:
    ordered_list = d.Bags.get_top(5000)
    counter = 0
    for bag in ordered_list:
        max_freq = -1
        most_freq_word = None
        for w in bag:
            freq = d[w][2]
            if freq > max_freq:
                most_freq_word = w
                max_freq = freq
        f. write(d.word(most_freq_word) + '\n')
        counter += 1
        if counter > 5000:
            break


d.get_most_frequent_in_bag()
