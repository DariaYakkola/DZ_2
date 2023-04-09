number = int(input('Введите трехзначное число: '))
handred = number // 100
ten = (number % 100) // 10
one = (number % 100) % 10
print(f'Cумма чисел равна - {handred + ten + one}')
