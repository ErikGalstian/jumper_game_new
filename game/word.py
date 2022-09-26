import random

class Word:
    def __init__(self):
        self.guess_word = []
        self.word_display = []
        self.hint = True
    def random_word(self):
        words = ["TABLET", "EARRING", "RING", "NECKLACE", "SCHOOL", "EDUCATION" , "UNIVERSITY" , "PRESIDENT"]
        self.guess_word = list(random.choice(words))
        for i in range(len(self.guess_word)):
            self.word_display.append(" _ ")
    def hint_correct(self, guess):
        count = self.guess_word.count(guess)
        if (count == 0):
            self.hint = False
        else:
            self.hint = True
            self.update_word_displayed(guess)
    def update_word_displayed(self, letter):
        for i in range(len(self.guess_word)):
            if self.guess_word[i] == letter:
                self.word_display[i] = letter
    def correct_word_hint(self):
        secret = "".join(self.guess_word)
        word = "".join(self.word_display)
        return secret == word
    def get_word_displayed(self):
        return " ".join(self.word_display)
    def last_hint(self):
        return self.hint

    
