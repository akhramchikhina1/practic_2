general_price=int(input('Введите общую стоимость часов: '))
quantity_gold=96/16
price_silver=((general_price-96*48)/int(quantity_gold))
print(round(price_silver))