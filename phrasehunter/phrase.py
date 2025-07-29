# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def __str__(self):
        return f'{self.phrase.title()}'
    

    def check_letter(self, guess):
        return guess in self.phrase
    

    def check_complete(self, guesses):
        guess_set = set(guesses)
        phrase_set = set(char for char in self.phrase if char != ' ')
        
        if len(guess_set) == len(phrase_set):
            return guess_set == phrase_set
        else:
            return guess_set.issuperset(phrase_set)
        

    def display(self, guesses):
        phrase_list = list(self.phrase)

        for i in range(len(phrase_list)):
            if phrase_list[i] not in guesses and phrase_list[i] != ' ':
                phrase_list[i] = '_'

            phrase_list[i] += ' '

        print(f'''
        {''.join(phrase_list)}

        ''')