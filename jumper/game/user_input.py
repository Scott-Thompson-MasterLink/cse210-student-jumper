import random
class userInput():
    
        def __init__(self):
            """Class constructor. Declares and initializes instance attributes.

        Args:
            self (userInput): An instance of userInput.
        """
            self.guess_letter = ''
            self.tries = 4
            self.guess = self.get_user_input()
            self.get_user_input()
            self.word = ''
            


        def get_user_input(self):
            """Gets an input from user for the userInput.

        Args:
            self (userInput): An instance of userInput.
        
        Returns:
            The letter the user did input and stores
        """
            guess = input('Guess letter [a-z]: ')
            self.guess = guess
            return self.guess

        def store_guesses_correct_or_incorrect(self):
            """Gets an input from user for the userInput.

        Args:
            self (userInput): An instance of userInput.
        
        Returns:
            The letter the user did input and stores
        """
                       
            if self.guess in self.word:
                return True
            else:
                return False
        
        def prevent_reguessing(self):
            
            self.guess_letter += self.guess
            return self.guess
            