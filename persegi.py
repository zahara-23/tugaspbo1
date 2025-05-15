class Persegi:
    def __init__(self):
        self.sisi = 0.0

def main():
    obj = Persegi()

    obj.sisi = 4

    luas = obj.sisi ** 2
    print('Luas persegi = %.2f' % luas)

if __name__ == '__main__':
    main()
