# if elif ornek

magaza=input("magaza ismini giriniz")
ciro=int(input("yapilan ciro ne kadar"))
limit=500
if ciro>limit:
    print("aferin "+magaza+" ciroyu "+str(ciro)+" ile gectin")
elif ciro==limit:
    print("sinirdasinnn, sinir:"+str(limit))
else:
    print("cok calis cok "+magaza)

