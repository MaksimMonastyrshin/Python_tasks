# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#   ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
#
# Перепишем выражение:
#
# not(x or y or z) = not(x) and not(y) and not(z)

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            left_expression = not(x or y or z)
            right_expression = not(x) and not(y) and not(z)
            print(x, y, z, left_expression == right_expression)
