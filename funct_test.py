def function_father(x) -> callable:
    
    def inside_function(repeat: int):
        print(x * repeat)

    return inside_function
        
first = function_father("hello")
second = function_father("world")

# first(1)
# second(2)
# first(3)

def double(func):
    def wrapper(a, b):
        return func(a, b) * 2
    
    return wrapper



from time import time, sleep

def time_measure(func):
    def wrapper(*args, **kwargs):
        before_execute = time()
        result = func(*args, **kwargs)
        after_exectute = time()
        print(f'{func.__name__} was called for {after_exectute - before_execute}')
        return result
    return wrapper


@double # sum = double(sum)
def sum(a,b):
    return a + b

@double
def sub(a,b):
    return a - b

def mut(a,b):
    sleep(1)
    return a * b


def decorator(mut):
    def mut_with_time(a, b):
        before_execute = time()
        result = mut(a, b)
        after_execute = time()
        func_time = after_execute - before_execute
        print(f'{mut.__name__} was called for {func_time}')
        return result
    return mut_with_time