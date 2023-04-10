print("Aan Susanto")
print("210511006")
print("Kelas R1")
print("="*40)

class Peneliti:
    def __init__(self, nama, judul):
        self.nama =  nama
        self.judul = judul
    
class Jurnal:
    def __init__(self, peneliti, judul):
        self.peneliti = peneliti
        self.judul = judul
    
    def judul_jurnal(self):
        for peneliti in self.peneliti:
            print(peneliti.peneliti, peneliti.judul)
    
jurnal1 = Jurnal("Aan Susanto","= " "Pengaruh Model Pembelajaran dengan Daring/Online")
jurnal2 = Jurnal("Budi","="" Yahahaaaaaaa")
jurnal = Jurnal([jurnal1, jurnal2], "kumpulan jurnal")
jurnal.judul_jurnal()