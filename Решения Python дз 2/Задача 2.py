naibolshaya_chastota=0
stroka=input("введите строку ")
for i in range(len(stroka)):
    symbol=(stroka[i])
    chastota=stroka.count(symbol)
    if chastota>naibolshaya_chastota:
        naibolshaya_chastota=chastota
        most_common=symbol
print(most_common)
