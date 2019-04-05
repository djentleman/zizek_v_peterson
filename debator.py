import markovify
from settings import (
    MARKOV_CHAIN_STATE_SIZE
)

def get_similarity(str1, str2):
    # return the percentage of the strings that overlap
    a = set(str1.lower().split(' '))
    b = set(str2.lower().split(' '))
    intersect = a.intersection(b)
    return float(len(intersect)) / (len(a) + len(b) - len(intersect))


class Debator():

    def __init__(self, name, corpus):
        self.name = name
        training_data = open(corpus).read()
        self.markov_model = markovify.Text(training_data, state_size=MARKOV_CHAIN_STATE_SIZE)

    def generate_point(self, count=1):
        point = ' '.join([self.markov_model.make_sentence()
                          for i in range(count)])
        return point

    def rebuttal(self, argument, count=1):
        counter_argument_pool_size = 10000
        potential_counter_arguments = [self.markov_model.make_sentence()
                                      for i in range(counter_argument_pool_size)]
        counter_arguments = sorted(potential_counter_arguments, key=lambda x: -get_similarity(x, argument))[:count]
        return ' '.join(counter_arguments)


