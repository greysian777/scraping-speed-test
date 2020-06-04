import timeit


def timer(num: int, n_repeat: int):
    """decorator to time function call"""

    def wrapper(fn):
        runs = timeit.repeat(fn, number=num, repeat=n_repeat)
        if n_repeat > 1:
            print(f"average {n_repeat} run time:", sum(runs) / len(runs))
        else:
            print('run time: ', sum(runs))

    return wrapper
