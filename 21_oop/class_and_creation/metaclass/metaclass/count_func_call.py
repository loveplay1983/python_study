def call_counter(func):

    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__
    return helper


if __name__ == '__main__':

    @call_counter
    def f():
        pass
    print(f.calls)


    for _ in range(10):
        f()

    print(f.calls)
