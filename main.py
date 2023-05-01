import time

def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

