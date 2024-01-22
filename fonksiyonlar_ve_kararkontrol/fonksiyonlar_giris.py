# karesini alan fonksiyon

def kare_al(x):
    print(x**2)
kare_al(5)


#bilgi notuyla cikti ureten fonksiyon
def kubu(y):
    print("girilen sayi:"+str(y)+
          " kubu:"+str(y**3))
    
kubu(4)

#iki argumanli fonksiyon
def carp(x,y):
    print(x*y)
carp(10,5)

#on tanimli argumanlar
def ikili_carp(x,y=1):
    print("x: "+str(x)+" y: "+str(y)+
          " carpim: "+str(x*y))
ikili_carp(3,4)
ikili_carp(y=3,x=6)
ikili_carp(x=5)
# ciktili fonksiyonlar
def direk(isi,nem,sarj):
    return (isi+nem)/sarj
sonuc=direk(50, 40, 15)
sonuc
