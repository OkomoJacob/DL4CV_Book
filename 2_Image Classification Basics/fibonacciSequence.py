n = int(input('Enter the last position to obtain in a Fibonaci sequence: '))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# using curly braces to dynamically insert values in your strings
msg = f'{fib(n)} is the {n+1}th number in a Fibonnacci Series'
print(msg)

