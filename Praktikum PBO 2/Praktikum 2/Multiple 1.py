class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang membuat program")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def presentasi(self):
        print(self.nama, "sedang presentasi")
mhs_pekerja = MahasiswaPekerja("Ahmad", "210511006", "Programmer")
mhs_pekerja.belajar() # output: Ahmad sedang belajar
mhs_pekerja.bekerja() # output: Ahmad sedang bekerja
mhs_pekerja.presentasi() # output: Ahmad sedang presentasi