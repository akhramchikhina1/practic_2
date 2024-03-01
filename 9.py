quantity=str(input('Введите количество быков и семей: '))
quantity=quantity.split(' ')
n=int(quantity[0])
k=int(quantity[1])
if n==0:
    print('0')
else:
    total=n%k
    print(total)