# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
day_31 = [1, 3, 5, 7, 9, 11]
day_30 = [4, 6, 8, 10, 12]
day_28 = [2]
while True:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)
    print('Вы ввели', month)
    if month in day_28:
        print('28 дней')
        break
    elif month in day_30:
        print('30 дней')
        break
    elif month in day_31:
        print('31 день')
        break
    else:
        print('Ошибка, повторите ввод')


# TODO здесь ваш код
# """31 день = Январь, Март, Май, Июль, Сентябрь, Ноябрь
# 30 дней = Апрель, Июнь, Август, Октябрь, Декабрь
# 28 дней = Февраль"""
# day_31 = [1, 3, 5, 7, 9, 11]
# day_30 = [4, 6, 8, 10, 12]
# day_28 = [2]
# if month in day_28:
#     print('28 дней')
# elif month in day_30:
#     print('30 дней')
# elif month in day_31:
#     print('31 день')
# else:
#     print('Ошибка, повторите ввод')