from urllib.request import urlopen
import re
import random

class Word:
    """The class word is going to select the word from
    an external .txt file, will check if letter guesses 
    are part of the word and will maintain word.
    


    Attributes:
        word (dictionary): key being the word to guess, and pair being the '_'
        under_guesses (list): list of underscores. Same quantity of the word's index
        link (list): list of 10000 words extracted from a link
        list_words (list): list of word tha have more than 5 letters
    """

    def __init__(self):
        """The class constructor.
        
         Args:
            self (Word): An instance of Word.
        
        """
        self.word = ''
        self.under_guesses = None
        self.link = urlopen('https://www.mit.edu/~ecprice/wordlist.10000').read().splitlines()
        self.list_words = []

        for i in self.link:
            if len(i) >= 5:
                self.list_words.append(i.decode('utf-8'))

        self.word = random.choice(self.list_words)
        self.under_guesses = ['_'] * len(self.word)

    
    def verify_guess(self, guess):
        """
        
        Args:
            self (Word): an instance of Word.
            guess(str): guesses of the user.
        """

        x = re.finditer(f'[{guess}]+', self.word)
        match = [match.start() for match in x]

        for i in match:
            self.under_guesses[i] = f'{guess}'