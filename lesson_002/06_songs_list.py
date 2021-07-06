#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
# TODO здесь ваш код
song_1 = violator_songs_list[3][1]
song_2 = violator_songs_list[5][1]
song_3 = violator_songs_list[8][1]
all = int(song_1 + song_2 + song_3)
all_2 = int(((song_1+song_2+song_3) - all)*60)

print('Три песни звучат ' + str(all) + ' минут и ' + str(all_2) +' секунд')
# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
song_dict = violator_songs_dict['Sweetest Perfection'] +violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
song_dict_1 = int(song_dict)
song_dict_2 = int(((song_dict) - song_dict_1) * 60)

# TODO здесь ваш код
print('А другие три песни звучат ' + str(song_dict_1) + ' минут и ' + str(song_dict_2) + ' секунд')