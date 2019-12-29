import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


cProfile.run('fib(10)')
cProfile.run('fib(20)')
cProfile.run('fib(100)')

# test_fib(fib)
# python -m timeit -n 100 -s "import Task_03" "Task_03.fib(10)"
# 100 loops, best of 5: 18.4 usec per loop

# lesson_04>python -m timeit -n 100 -s "import Task_03" "Task_03.fib(15)"
# 100 loops, best of 5: 222 usec per loop

# python -m timeit -n 100 -s "import Task_03" "Task_03.fib(20)"
# 100 loops, best of 5: 2.46 msec per loop
