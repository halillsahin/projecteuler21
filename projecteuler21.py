bölentoplam=dict()
tambölenleri=[]
bölenlertoplamı=0
for i in range(2,10000):
    for r in range(1,i):
        if i%r==0:
            bölenlertoplamı+=r
            bölentoplam[i]=bölenlertoplamı
    bölenlertoplamı=0
for i,a in bölentoplam.items():
   if a!=i and a in bölentoplam and bölentoplam.get(a)==i:
       tambölenleri.append(a)

print(sum(tambölenleri))