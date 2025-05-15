class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def deskripsi_buku(self):
        print(f"Buku '{self.judul}' ditulis oleh {self.penulis}.")
        
buku1 = Buku("Belajar Python", "Ali")
buku1.deskripsi_buku()
