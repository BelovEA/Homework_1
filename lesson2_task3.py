#. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
#поместить строковые данные в словарь(11 - 12 - 1 - 2(зима), 3 - 4(весна) 5 - 6- 7 -8(лето) 9 - 10(осень))
month = int(input("введите месяц в виде целого числа(от 1 до 12): "))
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
     9: "autumn", 10: "autumn", 11: "winter", 12: "winter"}

if month in d:
    print(f"{month} - month is {d[month]}")
else:
    print("input correct number of month(1-12)!")
