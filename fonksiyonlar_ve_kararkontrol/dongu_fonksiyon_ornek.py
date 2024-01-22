# dongu ve fonksiyonlar

maaslar=[100,200,300,400]

def zam(x):
    x=x*20/100+x
    print(x)
    return x
z=0
zam(100)
for i in maaslar:
    maaslar[z]=zam(i)
    z=z+1
print("*********")
def dusuk_maas(x):
    print(x+x*50/100)

def yuksek_maas(x):
    print(x+x*10/100)

for i in maaslar:
    if i >=360:
        yuksek_maas(i)
    else:
        dusuk_maas(i)
