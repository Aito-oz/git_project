# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
y = 500
x = 100

y2 = 450
x2 = 150
RL = sd.random_number(0,150)
RL2 = sd.random_number()
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=RL)
    y -= 10
    if y < 50:
       break
    x = x + 10

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=RL2)
    y2 -= 10
    if y2 < 50:
       break
    x2 = x2 + 20

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
