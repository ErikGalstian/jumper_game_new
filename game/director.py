from game.game import Game
from game.jumper import Jumper
from game.word import Word

class Director:
    def __init__(self):
        # Initializes all the values
        self.playing = True
        self.game = Game()
        self.jumper = Jumper()
        self.word = Word()
    def start(self):
        #Starts game
        print("\nGame has begun. Try to guess the right word!")
        self.word.random_word()
        self.game.draw(self.jumper.parachute())
        while self.playing:
            self.input()
            self.update()
            self.output()
            self.choose()
    def input(self):
        #Guess a letter 
        guess = self.game.read_text("Guess a letter [a-z]: ")
        self.word.hint_correct(guess)
    def update(self):
        if (not self.word.last_hint()):
            self.jumper.update_parachute()
        if self.word.correct_word_hint() or not self.jumper.quantity_wrong_hints():
            self.playing = False
    def output(self):
        self.game.write_text(self.word.get_word_displayed())
        self.game.draw(self.jumper.parachute())
        if not self.playing:
            print("GAME OVER ♥")
    def choose(self):
        #Continue or end the game
        if not self.playing: 
            playing = input("Continue playing? [Y/N] ")
            if playing.capitalize() == "N":
                self.playing = False
                print("\nThanks for playing Jumper!\n")
            elif playing.capitalize() == "Y":
                exec(open("./__main__.py").read())
            else:
                print("\nSelect a correct letter")
                self.choose()

