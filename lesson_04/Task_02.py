import cProfile


def get_len(array):
    return len(array)


def get_sum(arrray):
    s = 0
    for i in arrray:
        s += i
    return s


def main():
    lst = [i for i in range(10000000)]
    a = get_len(lst)
    b = get_sum(lst)


cProfile.run('main()')
