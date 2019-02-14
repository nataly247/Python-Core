# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = int(input("Insert value a: "))
b = int(input("Insert value b: "))

print("So, value a = {} and value b = {}".format(a,b))

print("Let\'s swap places!")
a, b = b, a
print("Now value a =", a)
print("And value b =", b)