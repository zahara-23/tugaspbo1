class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    
    def info_mobil(self):
        print(f"Mobil {self.merk} keluaran tahun {self.tahun}.")
        
mobil1 = Mobil("Toyota", 2020)
mobil1.info_mobil()
