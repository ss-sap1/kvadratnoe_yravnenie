print("Введите коэффициенты для квадратного уравнения (ax**2 + bx + c = 0):")
while True:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a or b or c == "" or a or b or c == 0:
        print("Число не может быть 0 или пустым. Введите число")
        continue

# a = float(1)
# b = float(-3)
# c = float(-4)
#
# import math
#
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")