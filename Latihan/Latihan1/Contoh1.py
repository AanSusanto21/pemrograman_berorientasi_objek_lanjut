#Nama: Nisa Uzufatul Jannah
#NIM : 210511001

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("Ferrari", "Hitam")
mobilA.info() # Output: Ferarri berwarna Hitam