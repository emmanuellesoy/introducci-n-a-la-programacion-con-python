def factorial_f(x): 
    # x = 5 | 4 | 3 | 2 | 1
    print("x = ", x)
    if x == 1:
        print("return value = ", 1)
        return 1
    else:
        return_value = x * factorial_f(x-1)
        print("return value = ", return_value)
        return return_value
        # 5 * 24 | 4 * 6 | 3 * 2 | 2 * 1


num = 5
factorial_f(num)
#print("The factorial of", num, "is", factorial_f(num))

n = 5
factorial = 1

while n >= 1:
    factorial = factorial * n
    n = n - 1
    
#print(factorial)
