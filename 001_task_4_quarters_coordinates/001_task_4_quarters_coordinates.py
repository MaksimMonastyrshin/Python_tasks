# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

q = int(input('Введите номер четверти (1-4): '))

if q == 1:
    print('1 четверть имеет диапазон координат: X > 0, Y > 0')
elif q == 2:
    print('2 четверть имеет диапазон координат: X < 0, Y > 0')
elif q == 3:
    print('3 четверть имеет диапазон координат: X < 0, Y < 0')
elif q == 4:
    print('4 четверть имеет диапазон координат: X > 0, Y < 0')
else:
    print('Четверти задаются числами от 1 до 4. Попробуйте еще раз.')
