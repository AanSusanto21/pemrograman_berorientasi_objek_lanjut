class Manusia:
    def __init__(self, Nama):
        self.Nama = Nama
    
    def Berbicara(self):
        print(f"{self.Nama} berbicara sendiri")

class Orang(Manusia):
    def __init__(self, Nama, Kulit):
        super().__init__(Nama)
        self.Kulit = Kulit
    
    def Bertanya(self):
        print(f"{self.Nama} kulitnya {self.Kulit}")

class Mahasiswa(Orang):
    def __init__(self, Nama, Kulit, Bahasa):
        super().__init__(Nama, Kulit)
        self.Bahasa = Bahasa
    
    def Berbicara(self):
        print(f"{self.Nama} berbicara bahasa {self.Bahasa}")
        
Mahasiswa = Mahasiswa("Aan Susanto", "Sawo muda", "Sunda")
Mahasiswa.Berbicara()
Mahasiswa.Bertanya()