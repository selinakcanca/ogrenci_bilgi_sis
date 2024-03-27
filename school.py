class Student:

 def __init__(self, isim, soyAd, katilim, sinif) -> None:
    self.isim = isim
    self.soyAd = soyAd
    self.sinif = sinif
    self.katilim = katilim
    self.vize = 0
    self.final = 0

 def notEkle(self, vize, final):
        self.vize = vize
        self.final = final

 def öğrenciBilgi(self):
    return "{} {} isimli öğrencimiz {} da sinavlarina {} ve vize notu : {} final notu : {} şeklindedir.".format(
        self.isim,
        self.soyAd,
        self.sinif,
        "Katildi" if self.katilim else "Katilmadi",
        self.vize,
        self.final
    )
 def ortalamaHesapla(self):
        return (self.vize * 0.4) + (self.final * 0.6)


class Teacher:
    def __init__(self, isim):
        self.isim = isim

    def kanaatNotuEkle(self, öğrenci, kanaatNotu):
        yeni_ortalama = öğrenci.ortalamaHesapla() + kanaatNotu
        print(f"{öğrenci.isim} {öğrenci.soyAd} için yeni ortalama (Kanaat Notu Dahil): {yeni_ortalama}")
        return yeni_ortalama

    #Bir öğrenci bilgi sistemi oluşturun. Öğrencilerin notlarını, katılım durumlarını ve diğer akademik bilgilerini saklamak için 
    #bir sınıf oluşturun. vize final => ortalama hesabını + kanaat notu => öğretmende tutalım