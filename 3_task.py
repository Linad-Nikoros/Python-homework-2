# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
#  максимум использование библиотеки Random для и получения случайного int

from random import randint

list_1=[ 154, 22, 3, 5, 7, 89, 74, 2, 5, 87, 525, 285, 248, 796, 451, 566]

for i in range(0,len(list_1)-1):
    j=randint(0,len(list_1)-1)
    temp=list_1[j]
    list_1[j]=list_1[i]
    list_1[i]=temp

print(list_1)
