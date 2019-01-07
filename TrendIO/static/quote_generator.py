#Author: Piyush Sharma
#Date: Sometime in June or July 2018
#Generates a random quote from the list.

import random

class Quote:

    def generate(self):

        quotes = [
            'Its a beautiful day!',
            'Its a rainy day!',
            'You Look Sensational. Completely Honest.',
            'Even if you were cloned, you\'d still be one of a kind. And the better looking one',
            'The way you\'re smiling right now is proof that the best things in life are free.',
            'You\'re smarter than Google and Mary Poppins combined.',
            'Are you a beaver, because damn.',
            'Explore the home tab. You\'ll meet a lot of new people. Promise. :)',
        ]


        choice = random.choice(quotes)

        return choice

# Debugging and testing only
# if __name__==__main__:
#    quote_gen = Quote()
#
#   quote_gen.generate()
