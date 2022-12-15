# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

n = str(input('Введите число: '))
sum_digit = 0

for digit in n:
    if digit.isdigit():
        sum_digit += int(digit)

print("Сумма цифр: ", sum_digit)
