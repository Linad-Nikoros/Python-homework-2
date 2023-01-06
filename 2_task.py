#  Задайте список из n чисел последовательности (1 + 1/n)**n, 
#  выведеите его на экран, а так же сумму элементов списка.
num_1=int(input("Введите число: "))

list_1=[] 
sum_1=0

for i in range(1,num_1+1):
  list_1.append(round((1+1/i)**i,2))
  
for i in range(num_1):
  sum_1+=list_1[i]

print(list_1)
print(f'Сумма элементов списка: {sum_1}')