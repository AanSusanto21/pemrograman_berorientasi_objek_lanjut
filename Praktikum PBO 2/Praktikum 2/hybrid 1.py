class Grup:
    def __init__(self, Nama, Usia):
        self.Nama = Nama
        self.Usia = Usia
    
    def Info(self):
        print("Identitas\nNama: ",self.Nama)
        print("Usia: ", self.Usia)
    
class Membership(Grup):
    def __init__(self, Nama, Usia, Status):
        super().__init__(Nama, Usia)
        self.Status = Status

    def Info(self):
        super().Info()
        print("Status: ",self.Status)

class Member(Grup):
    def __init__(self, Nama, Usia, Jenis_Membership):
        super().__init__(Nama, Usia, Jenis_Membership)
        self.Jenis_Membership = Jenis_Membership
    
    def Info(self):
        super().Info() 
        print("Jenis_Membership: ", self.Jenis_Membership)

class Orang(Member, Membership):
    def __init__(self, Nama, Usia, Status, Jenis_Membership, Alamat):
        Member.__init__(self, Nama, Usia, Jenis_Membership)
        Membership.__init__(self, Nama, Usia, Status)
        self.Alamat = Alamat

    def Info(self):
        super().Info()
        print("Alamat: ",self.Alamat)

orang = Orang("Aan Susanto", "20", "Aktif", "VIP", "Kuningan")
orang.Info()