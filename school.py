class Student:

 def __init__(self, isim, soyAd, katilim, sinif) -> None:
    self.isim = isim
    self.soyAd = soyAd
    self.sinif = sinif
    self.katilim = True if katilim == "True" else False
    self.vize = 0
    self.final = 0

 def notEkle(self, vize, final):
    if self.katilim:
        self.vize = vize
        self.final = final
    else:
        print(f"{self.isim} {self.soyAd} sinavlara katilmadi.")

 def öğrenciBilgi(self):
    if self.katilim:
        return "{} {} isimli öğrencimiz {} sinifinda sinavlarina {} ve vize notu : {} final notu : {} şeklindedir.".format(
            self.isim, 
            self.soyAd, 
            self.sinif, 
            "Katildi" if self.katilim else "Katilmadi", 
            self.vize, 
            self.final)
    else:
        return f"{self.isim} {self.soyAd} isimli öğrencimiz {self.sinif} sinifinda sinavlara Katilmadi."
    
 def ortalamaHesapla(self):
    if self.katilim and self.vize is not None and self.final is not None:
        return (self.vize * 0.4) + (self.final * 0.6)
    else:
        print(f"{self.isim} {self.soyAd} sinavlara katilmadiği için ortalama hesaplanamiyor.")
        return None


class Teacher:
    def __init__(self, isim):
        self.isim = isim

    def kanaatNotuEkle(self, öğrenci, kanaatNotu):
        if öğrenci.katilim and öğrenci.vize is not None and öğrenci.final is not None:
            yeni_ortalama = öğrenci.ortalamaHesapla() + kanaatNotu
            print(f"{öğrenci.isim} {öğrenci.soyAd} için yeni ortalama (Kanaat Notu Dahil): {yeni_ortalama}")
            return yeni_ortalama
        else:
            print(f"{öğrenci.isim} {öğrenci.soyAd} sinavlara katilmadiği için kanaat notu eklenemez.")



    #Bir öğrenci bilgi sistemi oluşturun. Öğrencilerin notlarını, katılım durumlarını ve diğer akademik bilgilerini saklamak için 
    #bir sınıf oluşturun. vize final => ortalama hesabını + kanaat notu => öğretmende tutalım