import markovify
from settings import (
    MARKOV_CHAIN_STATE_SIZE,
    ADD_EXTRA_POINT
)
from nltk.corpus import (
    stopwords
)

en_stopwords = stopwords.words('english')

def get_similarity(str1, str2):
    # remove stop words
    str1 = [word for word in str1.lower().split(' ') if word not in en_stopwords]
    str2 = [word for word in str2.lower().split(' ') if word not in en_stopwords]
    # return the percentage of the strings that overlap
    a = set(str1)
    b = set(str2)
    intersect = a.intersection(b)
    return float(len(intersect)) / (len(a) + len(b))


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
        potential_counter_arguments = [argument
                                      for argument in potential_counter_arguments
                                      if argument != None]
        counter_arguments = sorted(potential_counter_arguments, key=lambda x: -get_similarity(x, argument))[:count]
        if ADD_EXTRA_POINT:
            counter_arguments = counter_arguments + [self.markov_model.make_sentence()]
        return ' '.join(counter_arguments)


