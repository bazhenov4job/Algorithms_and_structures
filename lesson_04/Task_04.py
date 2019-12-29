# Решение ряда Фибоначчи при помощи словаря

import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)


cProfile.run('fib_dict(10)')
# 19/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_dict(20)')
# 39/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_dict(100)')
# 199/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_dict(500)')
# 999/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)

# test_fib(fib_dict)

# python -m timeit -n 1000 -s "import Task_04" "Task_04.fib_dict(10)"
# 1000 loops, best of 5: 3.92 usec per loop

# python -m timeit -n 1000 -s "import Task_04" "Task_04.fib_dict(15)"
# 1000 loops, best of 5: 5.52 usec per loop

# python -m timeit -n 1000 -s "import Task_04" "Task_04.fib_dict(20)"
# 1000 loops, best of 5: 7.31 usec per loop

# python -m timeit -n 1000 -s "import Task_04" "Task_04.fib_dict(100)"
# 1000 loops, best of 5: 41.2 usec per loop

# python -m timeit -n 1000 -s "import Task_04" "Task_04.fib_dict(200)"
# 1000 loops, best of 5: 79.4 usec per loop
