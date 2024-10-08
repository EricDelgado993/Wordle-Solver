import random
import json

class AI_Player:

    def __init__(self):

      # Load word_list
        with open('wordle_list') as f:
          self.word_list = json.loads(f.read())

      # Initialize last_guess
        self.last_guess = ""

    def guess(self):

        # Choose a random word from the remaining possible words
        self.last_guess = random.choice(self.word_list)
        return self.last_guess

    def read_answer(self, green, yellow):

        # Table to store last_guess word information
        feedback = ['x', 'x', 'x', 'x', 'x']

        for x in yellow:
          feedback[x] = 'y'
        
        for x in green:
          feedback[x] = 'g'

        # Tuple structure to iterate through word_list
        temp_tuple = tuple(self.word_list)

        # Iterate through remaining words in word_list
        for word in temp_tuple:

          # Compare each character in last_guess word to word_list word
          for i in range(5):

            # Delete word in word_list with last_guess' gray character (single character occurrence)
            if feedback[i] == 'x' and self.last_guess[i] in word and self.last_guess.count(self.last_guess[i]) == 1:
              self.word_list.remove(word)
              break
          
            # Delete word in word_list with last_guess' gray character (double character occurrence)
            elif feedback[i] == 'x' and self.last_guess[i] in word and self.last_guess.count(self.last_guess[i]) == 2 and self.last_guess[i] == word[i]:
              self.word_list.remove(word)
              break

            # Delete word in word_list with last_guess' gray character (triple character occurrence)
            elif feedback[i] == 'x' and self.last_guess[i] in word and self.last_guess.count(self.last_guess[i]) == 3 and self.last_guess[i] == word[i]:
              self.word_list.remove(word)
              break

            # Delete word in word_list not containing last_guess' green character
            elif feedback[i] == 'g' and self.last_guess[i] != word[i]:
              self.word_list.remove(word)
              break
            
            # Delete word in word_list not containing last_guess' yellow character
            elif feedback[i] == 'y' and self.last_guess[i] not in word:
              self.word_list.remove(word)
              break

            # Delete word in word_list when last_guess' yellow character is in the same position as word's
            elif feedback[i] == 'y' and self.last_guess[i] == word[i]:
              self.word_list.remove(word)
              break