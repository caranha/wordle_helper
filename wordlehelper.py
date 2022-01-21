from string import ascii_lowercase
import re
from random import sample

dictionary = []
mask = []
ispart = []
with open("five_letter_words.txt", "r") as f:
    for word in f.readlines():
        dictionary.append(word[:-1])

# create mask: list of 5 [abcdef...z]
for i in range(5):
    mask.append("["+ascii_lowercase+"]")

dogame = True
while dogame:
    word = ""
    result = ""

    # Input Word
    # Input Result (1 - green,2 - yellow, 3 - other)
    doinput = True
    while doinput:
        word = input("Enter the word (5 letters): ")
        result = input("Enter the result (5 numbers, 1 is green, 2 is yellow, 3 is black): ")

        if re.match("[123]{5}", result) and re.match("[\w]{5}", word):
            doinput = False
        else:
            print("Error in the word or result. Please try again")

    # Update mask
    for i in range(5):
        if result[i] == "1": # Green -- hardmode
            mask[i] = word[i]
            if word[i] not in ispart:
                ispart.append(word[i])
        elif result[i] == "2": # Yellow -- remove letter from this mask, add letter to yellow
            mask[i] = re.sub(word[i], "", mask[i])
            if word[i] not in ispart:
                ispart.append(word[i])
        elif result[i] == "3": # Black -- remove from this mask, and from others if not yellow
            mask[i] = re.sub(word[i], "", mask[i])
            if word[i] not in ispart:
                for j in range(5):
                    mask[j] = re.sub(word[i], "", mask[j])

    # Update Dictionary
    new_dictionary = []
    tmask = "".join(mask)
    for w in dictionary:
        newdict = True
        for l in ispart:
            newdict = newdict and l in w
        newdict = newdict and re.search(tmask, w)
        if newdict:
            new_dictionary.append(w)

    dictionary = new_dictionary
    # List size of Dictionary
    # List 20 words in dictionary

    print("Remaining Words: {}".format(len(dictionary)))
    # print("Mask: {}".format("".join(mask)))
    if len(dictionary) <= 20:
        print(", ".join(dictionary))
    else:
        print(", ".join(sample(dictionary, 20)))
