#1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
name, age, country = input("What is your name? "), int(input("how old are you? ")), input("where are you from? ")
print("Hi", name, "!")
print("you are", age, "years")
print("I'm from", country, "too!")
#2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input("введите время в секундах: "))
h = sec // 3600
minutes = sec // 60 - h * 60
sec = sec % 60
print(f"{h:02}:{minutes:02}:{sec:02}")
#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("число n: "))
x = str(n)
x1 = x + x
x2 = x + x + x
x = int(n)
v = x + int(x1) + int(x2)
print("сумма чисел n = ", v)
#да, получилось громоздко, но опыта мало :(((

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num = int(input("введите целое положительное число: "))
max = 0
minimum = 9
while num > 0:
    last = num % 10
    if last > max:
        max = last
    if minimum > last:
        minimum = last
    num = num//10
print("самое больщое число из представленных: ", max)
print("самое маленькое число из представленных: ", minimum)

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
a = int(input("выручка фирмы: "))
b = int(input("издержки фирмы: "))
if a > b:
    print("выручка больше издержек на: ", a - b)
if a > b:
    rent = a / b
    print(f"рентабельность предприятия равна: {100 * (a / b):.2f}")
if a > b:
    c = int(input("введите кол-во сотрудников фирмы: "))
    print(f"прибыль фирмы в расчёте на одного сотрудника: {a / c:.2f}")
else:
    print("издержки больше выручки на: ", b - a)
# 6
a = int(input("результат в первый день пробежек: "))
b = int(input("результат в последний день пробежек: "))
x = 1
print("Результат:")
print(f'{x}-й день: {a}')
while a < b:
    x += 1
    a = a * 110 / 100
    print(f'{x}-й день: {a:.2f}')
    a = (a * 110) / 100
if a > b:
    print(f"Ответ: на {x}-й, день спортсмен достиг результата — не менее {b} км")
#
