# sinif tanimlama

class ilksinif():
    print("tanimlandi")
    
# siniflarin ozellikleri

class veri_bilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildigi_diller=[]
# siniflarin ozelliklerine erismek

veri_bilimci.sql
veri_bilimci.bolum
# siniflarin ozelliklerini degistirmek
veri_bilimci.sql='hayir'
veri_bilimci.sql

# sinif orneklemesi
leo=veri_bilimci()
leo.bildigi_diller.append("python")
leo.bildigi_diller
leo.sql

apa=veri_bilimci()
apa.bildigi_diller #leo ile ayni cikti!!

# sinif ozellikleri

class evdekiler():
    adres="aksaray"
    def __init__(self):
        self.isim=[]
        self.yas=[]
        self.tur=[]
    
leo=evdekiler()
leo.tur.append("kedi")
leo.yas.append(2)
leo.isim.append("kedicik")
apa=evdekiler()
apa.tur="kus"
apa.yas=10
apa.isim="kuscuk"
leo.tur
apa.tur
leo.adres = "aksaray_merkez"
leo.adres       
apa.adres
evdekiler.adres

