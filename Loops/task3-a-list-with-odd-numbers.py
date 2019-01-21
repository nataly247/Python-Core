#3. Перевірити чи список містить непарні числа.

list_number=[2,4,6,8,9,10]
contain_odd=False
for val in list_number:
    if not val % 2 == 0:
        contain_odd=True
        break
    print("A list contains odd numbers!")