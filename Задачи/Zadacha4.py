"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
x = 1000
y = 500
z = 10
print(f'Введите выручку фирмы: {x}')
print(f'Введите издержки фирмы: {y}')
print(f'Финансовый результат - прибыль. Ее величина:{x-y}')
print(f'Рентабельность выручки = {(x-y)/x}')
print(f'Введите численность сотрудников фирмы: {z}')
print(f'Прибыль фирмы в расчете на одного сотрудника = {(x-y)/z}')