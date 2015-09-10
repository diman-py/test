def hello():
    print('Hello!')
    
def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b