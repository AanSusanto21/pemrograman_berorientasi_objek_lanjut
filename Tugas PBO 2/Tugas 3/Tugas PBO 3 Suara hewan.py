from playsound import *

class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Anjing(Animal):
    def make_sound(self):
        print("Anjing")
        playsound("anjing.mp3")

class Ayam(Animal):
    def make_sound(self):
        print("Ayam")
        playsound("ayam.mp3")

class Gajah(Animal):
    def make_sound(self):
        print("Gajah")
        playsound("gajah.mp3")

class Elang(Animal):
    def make_sound(self):
        print("Elang")
        playsound("elang.mp3")

class Kelelawar(Animal):
    def make_sound(self):
        print("kelelawar")
        playsound("kelelawar.mp3")

class Kucing(Animal):
    def make_sound(self):
        print("kucing")
        playsound("kucing.mp3")

class Banteng(Animal):
    def make_sound(self):
        print("Banteng")
        playsound("banteng.mp3")

class Serigala(Animal):
    def make_sound(self):
        print("Serigala")
        playsound("serigala.mp3")

class Burung(Animal):
    def make_sound(self):
        print("Burung")
        playsound("burung.mp3")

class Ular(Animal):
    def make_sound(self):
        print("Ular")
        playsound("ular.mp3")

def animal_sound(Animal):
    Animal.make_sound()


animal = Animal()
anjing = Anjing()
ayam = Ayam()
gajah = Gajah()
elang = Elang()
kelelawar = Kelelawar()
kucing = Kucing()
banteng = Banteng()
serigala = Serigala()
burung = Burung()
ular = Ular()

animal_sound(elang)