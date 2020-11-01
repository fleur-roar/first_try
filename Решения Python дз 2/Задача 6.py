n=int(input("Введите число "))
k=1
from math import sqrt
koren=sqrt(n)
conec=int(koren)
for k in range (1,conec+1):
    if k**2<=n:
        print(k**2)
