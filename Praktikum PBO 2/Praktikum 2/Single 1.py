class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "Singa Atlas bergerak")
        
class Singa(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Aaarrrr!")

singaA = Singa("Aaarrrr", 2, "Atlas")
singaA.bergerak() # output: Singa Atlas bergerak
singaA.bersuara() # output: Aaarrrr!