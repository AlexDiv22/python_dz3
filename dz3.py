#1 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2]))


#2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random
# number = int(input('Введите количество чисел в списке: '))
# list_number = list(random.randint(0, 10) for i in range(number))
# print(list_number)
# multiplication_number = list(list_number[i]*list_number[-1*(1+i)] for i in range(number//2+1*(number%2)))
# print(multiplication_number)


#3 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# list = [1.1, 1.2, 3.1, 10.01]
# mix_list = []

# for i in list:
#     mix_list.append(round(i-int(i), 2))

# print(list, end=' => ')
# print(max(mix_list) - min(mix_list))


#4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a=int(input('Введите число: '))
# b=bin(a)
# print('В двоичном виде выглядит так:', b[2:])


#5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

fibonacci_number = int(input('Введите любое натуральное число: '))
result = []
for i in range(fibonacci_number+1):
    if i==0:
        result.append(i)
    elif i==1:
        result.append(i)
        result.insert(0, i)
    else:
        result.append(result[len(result)-1]+result[len(result)-2])
        result.insert(0, (-1)**(i-1)*result[len(result)-1])
print(f'Список чисел Фибоначчи для {fibonacci_number}: {result}')