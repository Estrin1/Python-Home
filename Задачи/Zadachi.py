"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
x = 10
y = 'string empty'
c = 3.25
print(x)
print(y)
print(c)
print("Введите Ваше имя:")
w = str(input())
print("Введите Ваш пароль:")
z = str(input())
print("Введите Ваш возраст :")
x = int(input())
print(f'Ваши данные для входа в аккаунт: имя - {w}, пароль - {z}, возраст - {x}')

