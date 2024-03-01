quantity=str(input('Введите количество друзей и конфет: '))
quantity=quantity.split(' ')
n=int(quantity[0])
m=int(quantity[1])
peoples=n+1
if m==0:
    print('0')
else:
    total=m//peoples
    print(total)