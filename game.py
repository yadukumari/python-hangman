from hangman import *
import random


class Game:
    def __init__(self):
        self.hangman = Hangman()
        self.theme_name = ["animals", "clothes"]
        self.theme = input("Enter the theme you are interested: animals, clothes: ")
        while not (self.theme in self.theme_name):
            self.theme = input("Enter the theme you are interested: animals, clothes: ")
        self.words_list = []
        self.actual_word = ''
        self.guess_word = []
        self.unique_letters = []
        self.hangman.draw_frames()
        with open(self.theme + ".txt") as self.words:
            for i in self.words:
                i = i.rstrip()
                self.words_list.append(i)

    def choose_randomly(self):
        random.seed()
        searching_word = random.choice(self.words_list)
        self.actual_word = searching_word
        underscore_word = len(self.actual_word) * "_ "
        self.guess_word = underscore_word.split()

    def print_underscore(self):
        delimiter_space = ''
        print(delimiter_space.join(self.guess_word))

    def draw_hangman_game(self, num):
        if num == 5:
            self.hangman.draw_head()
        elif num == 4:
            self.hangman.draw_body()
        elif num == 3:
            self.hangman.draw_left_hand()
        elif num == 2:
            self.hangman.draw_right_hand()
        elif num == 1:
            self.hangman.draw_left_leg()
        elif num == 0:
            self.hangman.draw_right_leg()
        else:
            print("bye")

    def play_loop(self):
        choice = "y"
        while choice == "y":
            self.unique_letters = set()
            self.choose_randomly()
            self.print_underscore()
            chances = 5
            while chances >= 0:
                if "_" in self.guess_word:
                    guess_character = input("Guess the letter of the word: ")
                    if guess_character not in self.unique_letters:
                        self.unique_letters.add(guess_character)
                    else:
                        print("You already guessed", guess_character)
                        continue
                    delimiter_space = ' '
                    print("Already used letters: ", delimiter_space.join(self.unique_letters))
                    if guess_character in self.actual_word and guess_character not in self.guess_word:
                        for i in range(len(self.actual_word)):
                            if guess_character == self.actual_word[i]:
                                self.guess_word[i] = guess_character
                    else:
                        self.draw_hangman_game(chances)
                        chances -= 1
                        print("Remaining chances =", chances)
                else:
                    print("Congratulations")
                    break
                self.print_underscore()
            if "_" in self.guess_word:
                print("Good Try, the word is: ", self.actual_word)

            choice = input("Do you want to play again y/n: ")


if "__name__ = __main":
    G = Game()
    G.play_loop()
