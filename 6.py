weight=float(input('Введите вес (в фунтах): '))
high=float(input('Введите рост (в дюймах): '))
weight_kg=weight/2.205
high_metr=(high/39.3701)/100
imt=weight_kg/(high_metr**2)
print(round(imt, 2))