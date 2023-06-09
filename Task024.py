'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
'''

n = int(input("Введите количество кустов: "))
new_list = []
for i in range(n):
    new_list.append(int(input(f"Введите количество ягод на {i} грядке: ")))

print(new_list)
result_list = []
result_list.append(new_list[-1] + new_list[0] + new_list[1])
for i in range(1, len(new_list) - 1):
    result_list.append(new_list[i - 1] + new_list[i] + new_list[i + 1])
result_list.append(new_list[-2] + new_list[-1] + new_list[0])
max = 0
for i in result_list:
    if i > max:
        max = i
print(max)