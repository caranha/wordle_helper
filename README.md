# About

Quick and dirty script that generates suggestions for the [Wordle](https://www.powerlanguage.co.uk/wordle) game based on past hints.

One of the goals of this project is to show how you can write useful python scripts to students in my "Programming Intro" course, so the code purposely does not use some more advanced features and patterns in python.

Aside of the dictionary files, this code is in the public domain.

# Files

- `wordlehelper.py`: Main script. Loads dictionary from `five_letter_words.txt`, asks for wordle hints through the command prompt, and suggests new words based on the hints and the dictionary. Follows "hard mode" rules (which are actually easier to program)
- `five_letter_words.txt`: Dynamically created by the `*2fiveletter.py` scripts. Contains word dictionary.

- `getOPTED.py`: Downloads the [Public Domain Text Dictionary (OPTED)](https://www.mso.anu.edu.au/~ralph/OPTED/) and save it in the `OPTED` folder. Please only use it once.
- `OPTED2fiveletter.py`: Generates 5 letter dictionary from OPTED dictionary files. NOTE: the OPTED dictionary is from 1920, so it is not very useful for Wordle. I'm leaving it here as a demonstration of how to scrape HTML files.

- `wamerican2fiveletter.py`: Generates 5 letter dictionary from the `wamerican` package dictionary. See details in the `wamerican` folder.

- `LICENSE.md`, `LOG.md`, `README.md`: Documentation.


# Possible Improvements:

- Improve command line prompt: Script does not end properly, and maybe prompt is too confusing?
- Find other dictionaries: Wordle's dictionary has 10.000 words. needs at least that many. Maybe merge current dictionaries.
- Make more Pythonic version: Current code is quite ugly
- Sort word suggestions by some metric: Currently they're just random.
- Add [CMU dictionary](http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/)
