# local ve global degiskenler

x=10
y=5

def carp(x=2,y=4):
    return x*y
carp(1,5)
carp(x,y)

#local alandan global e etki etmek

liste=[]

def ekle(y):
    liste.append(y)
    print(str(y)+" listeye eklendi")

ekle("leo baba")
liste
