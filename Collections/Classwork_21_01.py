# Colletions

# 1. Створити список цілих чисел, які вводяться з терміналу (?)
# та визначити серед них максимальне та мінімальне число

# create empty list:
# list[]

# to make user Input numbers (5 for example)
# while i < 5:
#     print("Input number: ")

# to take user input and convert it from string to integer
# n = int(print("Input number: "))

# HOW to take every input (?)

# add to list
# list.append(those numbers)

# Having a list find min and max values
list = [1, 5, 80, 52, 17]
x = max(list)
y = min(list)
print("The biggest number is", x)
print("The smallest number is", y)

# 2. В інтервалі від 1 до 10 визначити числа
#    - парні, які діляться на 2,
#    - непарні, які діляться на 3,
#    - числа, які не діляться на 2 та 3.

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)
odd = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 0]
print(odd)
number = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 1]
print(number)


# Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)
