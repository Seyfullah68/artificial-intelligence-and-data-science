# miras yapilari

class employees():
    def __init__(self):
        self.name=""
        self.surname=""
        self.expeience=""
    def exp(self,x):
        self.expeience=x

class engineers(employees):
    def __init__(self):
        self.programing=""

class managers(employees):
    def __init__(self):
        self.department=""

leo=engineers()
leo.name="kedi"
leo.surname="kedicik"
leo.exp(10)
apa=managers()
apa.name="kus"
apa.surname="papagan"
apa.exp(4)
leo.expeience
apa.surname

class isci():
    def __init__(self,isim,soyisim):
        self.isim=isim
        self.soyisim=soyisim
can=isci("can","man")
can.soyisim
