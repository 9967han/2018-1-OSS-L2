def fibonacci(num):
    #this function cacluate fibonacci
    if num > 1:
        return fibonacci(num-1) + fibonacci(num-2)
    else:
        return num
