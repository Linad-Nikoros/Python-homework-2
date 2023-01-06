#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num_1 = input("Введите вещественное число: ")

list_1=list(num_1)
sum_1=0

for i in range(len(list_1)):
    if list_1[i] == ',': 
       list_1.pop(i)
       break

for i in range(len(list_1)):
    list_1[i] = int(list_1[i]) 
    sum_1+=list_1[i]

print(f'Число {num_1} имеет сумму цифр: {sum_1}')



