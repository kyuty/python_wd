# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def _private():
    print 'this is _private define'

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    print ''
    print fib2(int(sys.argv[1]))
    _private()
