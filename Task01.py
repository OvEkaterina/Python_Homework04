# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел.
# 2 строка - второй список через пробел.

list_one = list( map (int, input().split()))
list_two = list( map (int, input().split()))
list_three = set(list_one).intersection(set(list_two))
print(list_three)
