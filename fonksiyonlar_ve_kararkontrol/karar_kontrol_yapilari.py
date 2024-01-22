# karar kontrol yapilari

sinir=180

sinir==120
sinir==180
gelir1= 250
gelir2=200
gelir3=300
orta=250
def olc(x):
    if x<orta:
        print("fakir")
    elif x==orta:
        print("orta duzey")
    else:
        print("zengin")
olc(gelir1)
olc(gelir2)
olc(gelir3)
