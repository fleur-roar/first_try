#Задача 9
a=input('Введите первое число ')
b=input('Введите второе число ')
c=input('Введите произведение этих чисел ')
a=int(a)
b=int(b)
c=int(c)
proizvedenie=a*b
if proizvedenie==c:
    print('молодец!')
else:
    print('Нет:( Правильный ответ',proizvedenie)
