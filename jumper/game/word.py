from urllib.request import urlopen
import re
import random

class Word:
    """The class word is going to select the word from
    an external .txt file, will check if letter guesses 
    are part of the word and will maintain word.
    


    Attributes:
        word (dictionary): key being the word to guess, and pair being the '_'
        guesses (list): list of the user's guesses during the game.

    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word = ''
        self.under_guesses = None
        #self.guesses = []

    def get_word(self):
        
        self.link = urlopen('https://www.mit.edu/~ecprice/wordlist.10000').read().splitlines()
        self.list_words = []

        for i in self.link:
            if len(i) >= 5:
                self.list_words.append(i.decode('utf-8'))

        self.word = random.choice(self.list_words)
        self.under_guesses = ['_'] * len(self.word)
    
    def verify_guess(self, guess):

        x = re.finditer(f'[{guess}]+', self.word)
        match = [match.start() for match in x]

        for i in match:
            self.under_guesses[i] = f'{guess}'

        
        # from game.word import Word

        # word_x = Word()
        # word_x.get_word()

        # print(word_x.word)

        # while word_x:
        #     guess = input('Guess: ')
        #     word_x.verify_guess(f'{guess[0]}')
        #     print(word_x.under_guesses)

        # self.under_guesses = '  '.join(self.under_guesses)