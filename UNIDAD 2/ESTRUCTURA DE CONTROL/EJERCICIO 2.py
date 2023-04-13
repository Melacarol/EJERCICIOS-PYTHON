lista=[]
num=0
while num != 100:
    num +=1
    print(num)
    lista.append(num)
print(lista)
for num in lista:
    if num%2==0:
        print(num)
for num in lista:
    if num%2==1:
        print(num) 

