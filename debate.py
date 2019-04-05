from debator import (
    Debator
)
import random

def main():
    debators = [
        Debator('Zizek', 'corpus/zizek.txt'),
        Debator('Peterson', 'corpus/peterson.txt')
    ]
    turns = 10
    for i in range(turns):
        debator = debators[i % len(debators)]
        if i == 0:
            argument = debator.generate_point(random.randint(1, 3))
            print('%s%s: %s' % (('\t\t\t\t' if i % len(debators) == 1 else ''), debator.name, argument))
        else:
            argument = debator.rebuttal(argument, random.randint(1, 3))
            print('%s%s: %s' % (('\t\t\t\t' if i % len(debators) == 1 else ''), debator.name, argument))
        print('')



if __name__ == '__main__':
    main()

