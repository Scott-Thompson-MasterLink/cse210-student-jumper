from game.graphic import Graphic
from game.user_input import userInput
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.graphic = Graphic()
        self.userinput = userInput()
        self.keep_playing = True
        self.word = Word()
        self.userinput.word = self.word.word
        print('  '.join(self.word.under_guesses)) 
        print()
        self.graphic.print_graphic(self.userinput.mistakes)
        print('^^^^^^^^^^')
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        

        print('correct word:')
        print(self.word.word)

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        print('previous guesses:')
        print(' '.join(self.userinput.guess_letter))
        self.userinput.get_user_input()

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        self.word.verify_guess(self.userinput.guess)
        self.userinput.check_mistakes()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """

        print('  '.join(self.word.under_guesses)) 
        print()
        self.graphic.print_graphic(self.userinput.mistakes)
        print('^^^^^^^^^^')
        self.keep_playing = (self.graphic.keep_playing)

        if ''.join(self.word.under_guesses) == self.word.word:
            print('You win')
            self.keep_playing = False
        elif self.userinput.mistakes == 4:
            print('You lost')
            self.keep_playing = False

