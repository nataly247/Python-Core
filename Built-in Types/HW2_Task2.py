# Задано чотирицифрове натуральне число. 
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число

num = str(input("Enter 4 digit number:"))
multiplic = 1
for i in num:
  multiplic *= int(i)
print("Multiplication is " + str(multiplic))
rev = str(num)
print("Reversed number is ", rev[::-1])
s = str(num)
print("Sorted number is ", sorted(s))