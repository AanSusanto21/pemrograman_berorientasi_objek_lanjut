print("Aan Susanto")
print("210511006")
print("Kelas R1")
print("="*40)

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.informasi = Informasi()
    
    def __repr__(self):
        return f'Nama: {self.nama}\nJenis: {self.jenis}'

class Informasi:
    def __init__(self):
        self.info = []
    
    def add_informasi(self, warna, spesies):
        self.info.append(warna)
        self.info.append(spesies)
    
    def delete_informasi(self, warna, spesies):
        self.info.remove(warna)
        self.info.remove(spesies)

class Harimau:
    def __init__(self, hewan):
        self.hewan = hewan

hewan = Hewan("Harimau Always Win", "Karnivora")
info = Informasi()
hewan.informasi.add_informasi("Warna: Orange belang hitam","Spesies: Predator")
print(repr(hewan))
print(hewan.informasi.info)