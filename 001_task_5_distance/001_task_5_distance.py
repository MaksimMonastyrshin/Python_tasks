# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Введите координату x точки A: '))
y1 = float(input('Введите координату y точки A: '))
x2 = float(input('Введите координату x точки B: '))
y2 = float(input('Введите координату y точки B: '))

s = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
s = round(s, 3)

print('A (', x1, ',', y1, '); B (', x2, ',', y2, ') -> ', s)
