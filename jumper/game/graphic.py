#from game.user_input import wrong_guesses

class Graphic():
    """The graphic class is to create and display the 'jumper' graphic for the player

    Attributes:
        wrong_0 (int): instance of graphic with zero wrong guesses from player.
        wrong_1 (int): instance of graphic with 1 wrong guess.
        wrong_2 (int): instance of graphic with 2 wrong guesses.
        wrong_3 (int): instance of graphic with 3 wrong guesses.
        wrong_4 (int): instance of graphic with 4 wrong guesses.
    """

    def __init__(self):
        """
        Args:
            self (Graphic): instance of Graphic class.
        """
        self.wrong_0 = (" ___  \n"
                        "/___\\\n"
                        "\   / \n"
                        " \ /  \n"
                        "  0   \n"
                        " /|\  \n"
                        " / \  \n"
        )

        self.wrong_1 = ("/___\\\n"
                        "\   / \n"
                        " \ /  \n"
                        "  0   \n"
                        " /|\  \n"
                        " / \  \n"
        )
        
        self.wrong_2 = ("\   / \n"
                        " \ /  \n"
                        "  0   \n"
                        " /|\  \n"
                        " / \  \n"
        )

        self.wrong_3 = (" \ /  \n"
                        "  0   \n"
                        " /|\  \n"
                        " / \  \n"
        )

        self.wrong_4 = ("  X   \n"
                        " /|\  \n"
                        " / \  \n"
        )
        self.keep_playing = True


    def print_graphic(self, wrong_guesses):
        """
        Args:
            self (Graphic): instance of Graphic class.
            wrong_guesses (int): number of times the player has guessed a letter incorrectly
        """
        if wrong_guesses == 0:
            print(self.wrong_0)
        elif wrong_guesses == 1:
            print(self.wrong_1)
        elif wrong_guesses == 2:
            print(self.wrong_2)
        elif wrong_guesses == 3:
            print(self.wrong_3)
        elif wrong_guesses == 4:
            print(self.wrong_4)
            self.keep_playing = False



# graphic = Graphic()
# graphic.print_graphic(4)

# print(
#     " ___  \n"
#     "/___\\\n"
#     "\   / \n"
#     " \ /  \n"
#     "  0   \n"
#     " /|\  \n"
#     " / \  \n"
# )