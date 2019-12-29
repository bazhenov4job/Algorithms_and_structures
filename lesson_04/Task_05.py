# Решение ряда Фибоначчи при помощи списка

import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]
    return _fib_list(n)


cProfile.run('fib_list(10)')
# 19/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_list(20)')
# 39/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_list(100)')
# 199/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)
cProfile.run('fib_list(500)')
# 999/1    0.000    0.000    0.000    0.000 Task_04.py:14(_fib_dict)

# test_fib(fib_list)

# python -m timeit -n 1000 -s "import Task_05" "Task_05.fib_list(10)"
# 1000 loops, best of 5: 7.78 usec per loop

# python -m timeit -n 1000 -s "import Task_05" "Task_05.fib_list(20)"
# 1000 loops, best of 5: 10.9 usec per loop

# python -m timeit -n 1000 -s "import Task_05" "Task_05.fib_list(100)"
# 1000 loops, best of 5: 38.3 usec per loop

# python -m timeit -n 1000 -s "import Task_05" "Task_05.fib_list(200)"
# 1000 loops, best of 5: 73.3 usec per loop

