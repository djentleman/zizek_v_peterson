from debator import (
    Debator
)

def main():
    zizek = Debator('Zizek', 'corpus/zizek.txt')
    for i in range(10):
        print(zizek.generate_point())

if __name__ == '__main__':
    main()

