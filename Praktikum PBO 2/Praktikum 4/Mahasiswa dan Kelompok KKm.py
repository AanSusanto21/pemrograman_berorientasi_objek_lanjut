print("Aan Susanto")
print("210511006")
print("Kelas R1")
print("="*40)

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def __repr__(self):
        return f'{self.nama} {self.nim}'
    
class Anggota:
    def __init__(self):
        self.anggotas = []
    
    def add_anggota(self, anggota):
        self.anggotas.append(anggota)

class Kel_KKM:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

mahasiswa1 = Mahasiswa("Aan Susanto", 210511006)
mahasiswa2 = Mahasiswa("Susanto Aan", 730115012)
mahasiswa = Anggota()
mahasiswa.add_anggota(mahasiswa1)
mahasiswa.add_anggota(mahasiswa2)
kelompok = Kel_KKM(mahasiswa)
print(repr(kelompok.mahasiswa.anggotas))