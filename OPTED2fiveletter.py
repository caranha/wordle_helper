import os
import re

from bs4 import BeautifulSoup
from string import ascii_lowercase

base_file = "OPTED/words_X.html"

fiveletter = []

for letter in ascii_lowercase:
    file = base_file.replace("X",letter)
    with open(file, "r") as f:
        html = f.read()

    words = BeautifulSoup(html, "html.parser").find_all("b")
    for w in words:
        wt = w.get_text().lower()

        length = len(wt) == 5
        duplicate = wt in fiveletter
        ascii = not re.search("[\W]", wt)

        if length and ascii and not duplicate:
            fiveletter.append(wt)

with open("five_letter_words.txt", "w") as f:
    for w in fiveletter:
        f.write(w+"\n")
