#1.  Роздрукувати всі парні числа менші 100
# (написати два варіанти коду: один використовуючи
# цикл while, а інший з використанням циклу for).

## for loop v1
for i in range(2,100,2):
    print (i)
else:
    print("The end")

## for loop v2
for i in range(100):
    if i % 2 == 0:
        print(i)


## while loop
j = 2
while j < 100:
    print(j)
    j += 2
else:
    print("The end")


