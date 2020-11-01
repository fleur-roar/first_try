a=int(input("Введите число"))
largest_number=0
while a>0:
    c=a%10
    if c > largest_number:
        largest_number=c
    a=a//10
print(largest_number)
        
