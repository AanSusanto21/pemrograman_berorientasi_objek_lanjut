class Tokoh:
    def __init__(self, nama, umur, tingkat):
        self.nama = nama
        self.umur = umur
        self.tingkat = tingkat
    
    def get_nama(self):
        return self.nama
    
    def get_umur(self):
        return self.umur
    
    def get_tingkat(self):
        return self.tingkat

class Gojo(Tokoh):
    def __init__(self, nama, umur, tingkat, teknik):
        super().__init__(nama, umur, tingkat)
        self.teknik = teknik
    
    def get_teknik(self):
        return self.teknik

class Itadori(Tokoh):
    def __init__(self, nama, umur, tingkat, jutsu):
        super().__init__(nama, umur, tingkat)
        self.jutsu = jutsu
    
    def get_jutsu(self):
        return self.jutsu
    
class Sukuna(Itadori):
    def __init__(self, nama, umur, tingkat, jutsu, jeniskelamin):
        super().__init__(nama, umur, tingkat, jutsu)
        self.jeniskelamin = jeniskelamin

    def get_jeniskelamin(self):
        return self.jeniskelamin