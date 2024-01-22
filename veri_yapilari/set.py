# set 

#setler sirasizdir ve tek deger icerir, degerleri tekrar etmez
#setler hizli islemler icin kullanilir,sirasizdir

dizi=["ali","at","bak","ali","at"]
s= set(dizi)
s
t=(11,"veli","leo",11)
s= set(t)
s
t[0]
dizi[1]
s[0]
 #eleman ekleme cikarma
 
 dir(s)
s.add("naber")
s
s.add(11)
s
s.remove("11")
s
s.discard(11)#silme islemi yapar ama eleman zaten yoksa hata vermez
s
