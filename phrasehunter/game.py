from phrasehunter.phrase import Phrase
from phrasehunter.books import most_challenged_90s, most_challenged_00s, most_challenged_10s
import re
import random


def set_phrases():
    book_titles = []
    for item in most_challenged_90s + most_challenged_00s + most_challenged_10s:
        book_titles.append(item['title']) 
    
    filtered_titles = []
    for title in book_titles:
        # only add if book title is more than one word and has no special characters
        if re.fullmatch(r'([A-Za-z]+ [A-Za-z]+)( [A-Za-z]+)?', title):
            filtered_titles.append(title)
    
    return set(filtered_titles)


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = list(set_phrases())
        self.active_phrase = None
        self.guesses = []


    def welcome(self):
        print('''
              
Welcome to Phrase Hunter: Challenged Book Edition
-------------------------------------------------
''')


    def get_random_phrase(self):
        return Phrase(random.choice(self.phrases)) 


    def get_guess(self):
        self.give_feedback(self.missed, self.guesses)
        guess = input('\n>> Guess a letter: ').lower()
        guess_error = True
        while guess_error:
            # check that user input is a letter
            if re.fullmatch(r'[A-Za-z]', guess):
                if guess not in self.guesses:
                    self.guesses.append(guess)
                guess_error = False
                return guess
            else:
                print('''
                    ** Guesses must be a single letter. Try again. **
                    ''')
                self.give_feedback(self.missed, self.guesses)
                guess = input('\n>> Guess a letter: ').lower()


    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()

        while True:
            self.active_phrase.display(self.guesses)
            guess = self.get_guess()
            correct = self.active_phrase.check_letter(guess)

            if not correct:
                self.missed += 1
            
            if self.missed == 5:
                self.game_over('lost')
                break
            elif self.guesses and self.active_phrase.check_complete(self.guesses):
                self.game_over('won')
                break

        play_again_error = True
        while play_again_error:
            play_again = input('>> Do you want to play again? (Y/N)  ')
            if play_again.lower() == 'y':
                play_again_error = False
                return True
            elif play_again.lower() == 'n':
                print('\n\nThanks for playing.\n\n')
                play_again_error = False
            else:
                print('''
                    ** Please enter Y to play again or N to quit. **
                    ''')

    def give_feedback(self, missed, guesses):
        print(f'\nRemaining Misses: {5 - missed}')
        if guesses:
            print(f'Already Guessed: {', '.join(guesses)}')
        print('--------------------')


    def game_over(self, result):
        if result == 'won':
            print(f'''
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *                  
Congrats! You guessed it with only {self.missed} wrong guess(es).
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
                  ''')
        else:
            print('''
Bummer, you ran out of guesses. Better luck next time.
x   x   x   x   x   x   x   x   x   x   x   x   x   x 
                  ''')
        
        print(f'The challenged book was: {self.active_phrase}.\n\n')