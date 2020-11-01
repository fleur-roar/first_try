slovo=input("введите слово")
vowels="уаеиыяоэюё"
counter=0
for letter in slovo:
    if letter in vowels:
        counter+=1
print(counter)
