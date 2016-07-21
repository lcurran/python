# Fibonacci
a, b = 0, 1
while b < 200:
    print b,
    a, b = b, a+b

# iterate over strings
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)

# nested iterators to find prime number, demonstrate how break prevents else from
# executing
for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

# defining a function
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.""" #docstring print with __doc__
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)

# can access module name with ultra private method __name__

class MyClass:
    """A simple example class"""
    i = 12345

    # def __init__(self):
    #     self.data = []

    def f(self):
        return 'hello world'

# can change value of i by assignment

# creating class instance
x = MyClass()



# more demos http://www.hlevkin.com/Shell_progr/hellopython.htm
