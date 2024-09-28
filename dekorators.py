def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Декоратор активирован!")
        result = func(*args, **kwargs)
        print("Декоратор завершён!")
        return result
    return wrapper

def example_function():
    print('hello world')


example_function()