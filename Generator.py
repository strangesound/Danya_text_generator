import random
import numpy
s = open('text.txt')

s =  "".join([i for i in s if (i.isalpha() or i == " ")])
for i in s:
    i = i.lower()
word_list = s.split()

# словаря: {слово : [одно-следующее-слово, другое-следующее-слово, ...]}

next_words_dict = {}

for word, next_word in zip(word_list, word_list[1:]):
    if word not in next_words_dict:
        next_words_dict[word] = [next_word]
    else:
        next_words_dict[word].append(next_word)

next_words_dict_p = {}
for word, next_word in zip(word_list, word_list[1:]):
    if word not in next_words_dict:
        next_words_dict_p[word] = {next_word: 1}
    elif word in next_words_dict_p:
        if next_word in next_words_dict_p[word]:
            next_words_dict_p[word][next_word] += 1
    else:
        next_words_dict_p[word] = {next_word: 1}

for key in next_words_dict.keys():
    next_probs = next_words_dict[key]
    total = sum(next_probs.values())
    next_probs = {key: val / total for key, val in next_probs.items()} 
probobilites = next_probs.values()
sentence_len = random.randint(10, 15)
random_sentence = ""

seed = numpy.random.choice(next_probs, size=len(next_probs), p=probobilites)

random_sentence += seed
print(random_sentence)
