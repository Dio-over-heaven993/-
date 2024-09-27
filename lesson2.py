#1
a, b = map(float,input().split())
if b==0:
     print('Error, its impossible to divide by zero')
else:
     print(round(a/b, 2))

#2
summa = int(input())
if summa > 20:
    print(f'стоимость составила {round(summa - (summa * 0.35), 2)}, ваша скидка 35%')
else:
   print('скидки нет')
#3
a = int(input())
n = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1 <= a <= 12:
    if 9 <= a < 12:
        print(f'это {n[a]}, осень')
    elif 3 <= a < 6:
        print(f'это {n[a]}, весна')
    elif 6 <= a < 9:
        print(f'это {n[a]}, лето')
    else:
        print(f'это {n[a]}, зима')
else:
    print('такого месяца нет')