import random
class userInput():
    
        def __init__(self):
            """Class constructor. Declares and initializes instance attributes.

        Args:
            self (userInput): An instance of userInput.
        """
            self.guess_letter = []
            self.mistakes = 0
            self.guess = ''
            self.word = ''
            self.correct = None
            


        def get_user_input(self):
            """Gets an input from user for the userInput.

        Args:
            self (userInput): An instance of userInput.
        
        Returns:
            The letter the user did input and stores
        """
            guess = input('Guess letter [a-z]: ')
            self.guess = guess
            self.guess_letter.append(guess)


        def check_mistakes(self):
            """Gets an input from user for the userInput.

        Args:
            self (userInput): An instance of userInput.
        
        Returns:
            The letter the user did input and stores
        """
                       
            if self.guess in self.word:  
                print()
            else: 
                self.mistakes += 1
        
