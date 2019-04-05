import markovify
from settings import (
    MARKOV_CHAIN_STATE_SIZE
)

class Debator():

    def __init__(self, name, corpus):
        self.name = name
        training_data = open(corpus).read()
        self.markov_model = markovify.Text(training_data, state_size=MARKOV_CHAIN_STATE_SIZE)

    def generate_point(self):
        point = self.markov_model.make_sentence()
        return point

