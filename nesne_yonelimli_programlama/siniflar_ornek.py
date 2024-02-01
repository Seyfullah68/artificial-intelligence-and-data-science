# siniflar icin ornek

class calisanlar():
    is_yeri=[]
    def __init__(self):
        self.isim=""
        self.yas=[]
        self.tecrube=[]
    def tecrube_gir(self,x):
        self.tecrube.append(x)

leo=calisanlar()
apachi=calisanlar()
calisanlar.is_yeri="ev"
leo.isim="kedi"
leo.yas=2
leo.tecrube_gir(1)
apachi.isim="kus"
apachi.yas=10
apachi.tecrube_gir(9)
leo.tecrube
apachi.tecrube
leo.is_yeri
leo.isim
