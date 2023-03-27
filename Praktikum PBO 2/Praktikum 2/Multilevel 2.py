class Minuman:
    def __init__(self, nama):
        self.nama = nama
    
    def Rasa(self):
        print(f"{self.nama} rasanya manis dan enak")
    
class Jus(Minuman):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
    
    def Rasa(self):
        print(f"Buah ini {self.warna}")

class Mangga(Jus):
    def __init__(self, nama, warna, asal):
        super().__init__(nama, warna)
        self.asal = asal
    
    def Rasa(self):
        print(f"Mangga dari {self.asal}")

Mangga = Mangga("Mangga", "orange", "Bandung")
Mangga.Rasa()