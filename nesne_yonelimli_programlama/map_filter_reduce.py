# map fonksiyonu


liste=[1,2,3,4]

list(map(lambda x: x+10,liste))

#filter fonksiyonu

liste2=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2==0,liste2))

#reduce fonksiyonu

liste3=[1,2,3,4]

from functools import reduce

reduce(lambda a,b: a+b,liste3)
