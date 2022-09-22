from time import perf_counter
import random

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def run_step_1():
    n = int(input("Enter number of elements in array: "))
    l = []
    for i in range(n):
        l.append(random.randint(0, 10000))
    print(l)
    t_start = perf_counter()
    bubbleSort(l)
    t_stop = perf_counter()
    print(f"Elapsed Time: {t_stop-t_start}")
    print(l)

def run_step_2():
    n = int(input("Enter number of elements in array: "))
    l = []
    for i in range(n):
        l.append(random.randint(0, 10000))
    print(l)
    t_start = perf_counter()
    selectionSort(l, n)
    t_stop = perf_counter()
    print(f"Elapsed Time: {t_stop-t_start}")
    print(l)

def run_step_3():
    n = int(input("Enter number of elements in array: "))
    t_times = []
    for i in range(1000):
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        t_start = perf_counter()
        bubbleSort(l)
        t_stop = perf_counter()
        t_times.append(t_stop-t_start)
    t_time = 0
    for i in range(len(t_times)):
        t_time += t_times[i]
    print(f'Elapsed Time: {t_time}')

def run_step_4():
    n = int(input("Enter number of elements in array: "))
    t_times = []
    for i in range(1000):
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        t_start = perf_counter()
        selectionSort(l, n)
        t_stop = perf_counter()
        t_times.append(t_stop-t_start)
    t_time = 0
    for i in range(len(t_times)):
        t_time += t_times[i]
    print(f'Elapsed Time: {t_time}')
