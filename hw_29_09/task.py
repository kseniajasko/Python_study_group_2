from functools import wraps


def my_decorator(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    print(f'Я декоратор і я отримав аргументи: {signature}')
    def actually_decorator(func):
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            func(*func_args, **func_kwargs)
        return wrapper
    return actually_decorator


@my_decorator(2, 'This is Spartaaaaa!')
def say_hello():
    print('Hello World')


say_hello()
