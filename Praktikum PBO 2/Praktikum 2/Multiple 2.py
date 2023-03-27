class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Mamalia:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat
    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
class Kelenjar:
    def __init__(self, metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat
    def display_info(self):
        print(f"Metamorfosis: {self.metamorfosis}")
        print(f"Habitat: {self.habitat}")
class Lumba(Mamalia, Kelenjar):
    def __init__(self, nama, umur, jenis, habitat, metamorfosis):
        Hewan.__init__(self, nama, umur)
        Mamalia.__init__(self, jenis, habitat)
        Kelenjar.__init__(self, metamorfosis, habitat)
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        print(f"Metamorfosis: {self.metamorfosis}")
# contoh penggunaan
LumbaA = Lumba("Lumba_lumba", 40, "Mamalia-Kelenjar", "Air", "Tidak mengalami metamorfosis")
LumbaA.display_info()