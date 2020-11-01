n=int(input("Введите число "))
my_factorial=1
for i in range (1, n+1):
    my_factorial*=i
print(my_factorial)

#Не совсем поняла, нужно ли дословно выполнять то, что сказано в задании
#Сначала вывести, потом записать в my_factorial, потом еще раз вывести?
#Тогда просто
#otvet=1
#for i in range (1, n+1):
#   otvet*=i
#print(otvet)
#my_factorial=otvet
#print(my_factorial)
