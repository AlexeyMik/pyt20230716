# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
#  В заданном стринге из нулей и единиц подсчитаем отдельно кол-во нулей и единиц
#
s = None
while s== None :
    s = input("Введите слово из нулей и единиц: ")
n0 = 0
n1 = 0
for i in range (len(s)) :
    if s[i]=="0" : n0+=1
    if s[i]=="1" : n1+=1
print("кол-во нулей=",n0,"  кол-во единиц=",n1)
if n0==n1 :
    print("кол-во нулей равно кол-ву единиц")
elif n0>n1 :
    print("кол-во нулей больше кол-ва единиц")
else :
    print("кол-во нулей меньше кол-ва единиц")
