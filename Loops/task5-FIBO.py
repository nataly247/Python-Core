#5. Вивести числа Фібоначі включно до введеного числа n, 
# використовуючи цикли. 

num = int(input("Enter a number: "))

fib0 = 0
fib1 = 1
i = 1
while i < n:
    fib_sum = fib1 + fib0
    fib0 = fib1
    fib1 = fib_sum
    i += 1
 
print (fib_sum)
