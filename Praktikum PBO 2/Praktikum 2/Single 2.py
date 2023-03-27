class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Direktur(Manusia):
    def __init__(self, nama, umur, ruangan):
        super().__init__(nama, umur)
        self.ruangan = ruangan
    def mengajar(self):
        print(f"{self.nama} di ruangan {self.ruangan} sedang meeting.")
        
dosenA = Direktur("Ahmad", 35, "D.21")
dosenA.berbicara() # Output: Ahmad sedang berbicara.
dosenA.mengajar() # Output: Ahmad diruangan D.21 sedang meeting.