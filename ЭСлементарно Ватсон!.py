def number_addition():
    a = int(input("Введите число:"))
    b = 0
    while a > 0:
        c = a % 10
        b = b + a
        a = a // 10
    print('Сумма:', c)
number_addition()
