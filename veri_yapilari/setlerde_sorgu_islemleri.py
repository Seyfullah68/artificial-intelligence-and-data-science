# setlerde_sorgu_islemleri

set1=set([1,2,3])
set2=set([1,2,3,4,5])
#ortak eleman yok mu
set1.isdisjoint(set2)
#alt kumesi mi
set1.issubset(set2)
set2.issubset(set1)
#kapsiyor mu
set1.issuperset(set2)
set2.issuperset(set1)

