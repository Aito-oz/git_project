#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo.remove('elephant')

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
noil = zoo.index('lion')
kral = zoo.index('lark')
print('Лев сидит в ' +str(int(noil)+1) + ' клетке, а жаворонок в клетке номер ' + str(int(kral)+1))
print(zoo)


