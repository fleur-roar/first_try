#for n in range (1, 3):
#    print(n)
summa=0
stroka=input("введите строку ")
for i in range(len(stroka)):
    if stroka[i]==stroka[len(stroka)-1-i]:
        summa+=1
if summa==len(stroka):
    is_palindrom=True
else:
    is_palindrom=False
print(is_palindrom)

