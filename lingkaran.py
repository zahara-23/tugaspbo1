import math

class Lingkaran:
    def __init__(self):
        self.jari_jari = 0.0

def main():
    obj = Lingkaran()

    obj.jari_jari = 5
    
    luas = math.pi * (obj.jari_jari ** 2)
    print('Luas lingkaran = %.2f' % luas)

if __name__ == '__main__':
    main()
