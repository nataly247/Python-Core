# Functions

# Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі
# в залежності від вибору користувача )
PI = 3.14


def rectangle():
    a = float(input("Enter width: "))
    b = float(input("Enter length: "))
    print("Square = {}".format(a*b))


def triangle():
    a = float(input("Enter basis: "))
    h = float(input("Enter height: "))
    print("Square = {}".format(0.5 * (a * h)))


def circle():
    r = float(input("Enter radius: "))
    print("Square = {}".format(PI * (r ** 2)))


figure = input("1 - rectanle, 2 - triangle, 3 - circle - ")
if figure == "1":
    rectangle()
elif figure == "2":
    triangle()
elif figure == "3":
    circle()
else:
    print("Error input number")

# Написати функцію, яка обчислює суму цифр введеного числа.


def sum_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


number = int(input("Enter a number to calulate sum of its digits: "))
g = sum_digits(number)
print(sum_digits(number))

OR

number = int(input("Enter a number to calulate sum of its digits: "))
print(sum(map(int, str(number))))
