# Downloads the public domain "Online Plain Text English Dictionary"
# Please only run this once, if you need the files.

import requests
from time import sleep
from os import mkdir
from string import ascii_lowercase

base_url = "https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_X.html"

os.mkdir("OPTED")

for letter in ascii_lowercase:
    url = base_url.replace("X",letter)
    words = requests.get(url)
    with open("OPTED/words_"+letter+".html", "w") as out:
        out.write(words.text)
    sleep(0.1)
