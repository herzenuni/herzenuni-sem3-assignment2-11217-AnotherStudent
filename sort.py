from random import randint
import timeit

def bubble_sort(l):
    s = list(l)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] > s[j]):
            	s[i], s[j] = s[j], s[i]
    return s

def quick_sort(l):
    s = list(l)
    if l:
        head, *tail = l
        return quick_sort([x for x in tail if x <= head]) + \
               [head] + \
               quick_sort([x for x in tail if x > head])
    return []

def run_bubble_sort_small():
    bubble_sort([randint(-1000, 1000) for _ in range(100)])

def run_bubble_sort_big():
    bubble_sort([randint(-1000, 1000) for _ in range(10000)])

def run_quick_sort_small():
    quick_sort([randint(-1000, 1000) for _ in range(100)])

def run_quick_sort_big():
    quick_sort([randint(-1000, 1000) for _ in range(10000)])

if __name__ == '__main__':
    print('small bubble:', timeit.timeit('run_bubble_sort_small()',\
      setup = "from __main__ import run_bubble_sort_small", number = 3))

    print('big bubble:', timeit.timeit('run_bubble_sort_big()',\
      setup = "from __main__ import run_bubble_sort_big", number = 3))

    print('small quick:', timeit.timeit('run_quick_sort_small()',\
      setup = "from __main__ import run_quick_sort_small", number = 3))

    print('big quick:', timeit.timeit('run_quick_sort_big()',\
      setup = "from __main__ import run_quick_sort_big", number = 3))