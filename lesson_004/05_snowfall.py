# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
x1 = sd.random_number(0,600)
x2 = sd.random_number(0,600)
x3 = sd.random_number(0,600)
x4 = sd.random_number(0,600)
x5 = sd.random_number(0,600)
x6 = sd.random_number(0,600)
x7 = sd.random_number(0,600)
x8 = sd.random_number(0,600)
x9 = sd.random_number(0,600)
x10 = sd.random_number(0,600)
x11 = sd.random_number(0,600)
x12 = sd.random_number(0,600)
x13 = sd.random_number(0,600)
x14 = sd.random_number(0,600)
x15 = sd.random_number(0,600)
x16 = sd.random_number(0,600)
x17= sd.random_number(0,600)
x18= sd.random_number(0,600)
x19 = sd.random_number(0,600)
x20 = sd.random_number(0,600)
y1 = sd.random_number(0, 600)
y2 = sd.random_number(0, 600)
y3 = sd.random_number(0, 600)
y4 = sd.random_number(0, 600)
y5 = sd.random_number(0, 600)
y6 = sd.random_number(0, 600)
y6 = sd.random_number(0, 600)
y7 = sd.random_number(0, 600)
y8 = sd.random_number(0, 600)
y9 = sd.random_number(0, 600)
y10 = sd.random_number(0, 600)
y11 = sd.random_number(0, 600)
y12 = sd.random_number(0, 600)
y13 = sd.random_number(0, 600)
y14 = sd.random_number(0, 600)
y15 = sd.random_number(0, 600)
y1 = sd.random_number(0, 600)
y1 = sd.random_number(0, 600)
y1 = sd.random_number(0, 600)
y1 = sd.random_number(0, 600)

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point)

    pass
    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


