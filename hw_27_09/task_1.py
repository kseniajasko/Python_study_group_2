import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            start_time = time.perf_counter()
            func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Функція {func.__name__}({signature}) виконана за {run_time:.4f} секунд")
        except RuntimeError as e:
            print(str(e))
    return wrapper

@my_decorator
def sum_two_numbers(a, b):
    print(a + b)

#sum_two_numbers = my_decorator(sum_two_numbers)
sum_two_numbers(4, 15)