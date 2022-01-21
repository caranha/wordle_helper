import os
import re

from string import ascii_lowercase

fiveletter = []

with open("wamerican/words") as f:
    for wt in f.readlines():
        wt = wt[:-1].lower()

        length = len(wt) == 5
        duplicate = wt in fiveletter
        ascii = not re.search("[^{}]".format(ascii_lowercase), wt)

        if length and ascii and not duplicate:
            fiveletter.append(wt)

with open("five_letter_words.txt", "w") as f:
    for w in fiveletter:
        f.write(w+"\n")
