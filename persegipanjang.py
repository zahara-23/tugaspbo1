class PersegiPanjang:
    def __init__(self):
        self.panjang = 0.0
        self.lebar = 0.0

def main():
    obj = PersegiPanjang()
 
    obj.panjang = 6
    obj.lebar = 4

    luas = obj.panjang * obj.lebar
    print('Luas persegi panjang = %.2f' % luas)

if __name__ == '__main__':
    main()
