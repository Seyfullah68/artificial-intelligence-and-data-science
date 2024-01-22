# break ve continue

maaslar=[100,500,800,50,1000,1500,650]

dir(maaslar)
maaslar.sort()

for i in maaslar:
    if i==1000:
        break
    print(i)
for i in maaslar:
    if i==800:
        continue
    print(i)
        