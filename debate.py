from debator import (
    Debator
)

def main():
    zizek = Debator('Zizek', 'corpus/zizek.txt')
    peterson = Debator('Peterson', 'corpus/peterson.txt')
    for i in range(10):
        print(zizek.generate_point())
    print('---')
    for i in range(10):
        print(peterson.generate_point())

if __name__ == '__main__':
    main()

