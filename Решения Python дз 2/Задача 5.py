summa=0
poslednee_slagaemoe=1
for n in range(1,101):
    while poslednee_slagaemoe <= 2*n-1:
        summa += poslednee_slagaemoe
        poslednee_slagaemoe += 2
    if (summa==n**2):
        print("Это верно для числа", n)
    else:
        print("Это неверно для числа", n)
