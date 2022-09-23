from time import sleep, perf_counter
from threading import Thread
import random

global run1, run2, run3, run4, run5, run6
run1, run2, run3, run4, run5, run6 = [], [], [], [], [], []

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
    n = int(input("Enter number of elements in array for step 1: "))
    l = []
    for i in range(n):
        l.append(random.randint(0, 10000))
    print("Unsorted Array: ")
    print("     " + str(l))
    t_start = perf_counter()
    bubbleSort(l)
    t_stop = perf_counter()
    print("Sorted Array: ")
    print("     " + str(l))
    print(f"Elapsed Time for step 1: {t_stop-t_start: 0.6f}")
    return t_stop-t_start

def run_step_2():
    n = int(input("Enter number of elements in array for step 2: "))
    l = []
    for i in range(n):
        l.append(random.randint(0, 10000))
    print("Unsorted Array: ")
    print("     " + str(l))
    t_start = perf_counter()
    selectionSort(l, n)
    t_stop = perf_counter()
    print("Sorted Array: ")
    print("     " + str(l))
    print(f"Elapsed Time for step 2: {t_stop-t_start: 0.6f}")
    return t_stop-t_start

def run_step_3(a, n, run, j):
    t_times = []
    for i in range(a):
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        t_start = perf_counter()
        bubbleSort(l)
        t_stop = perf_counter()
        t_times.append(t_stop-t_start)

    t_time = sum(t_times)
    if run == 1:
        run1.append(t_time)
    elif run == 2:
        run2.append(t_time)
    elif run == 3:
        run3.append(t_time)

def run_step_4(a, n, run, j):
    t_times = []
    for i in range(a):
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        t_start = perf_counter()
        selectionSort(l, n)
        t_stop = perf_counter()
        t_times.append(t_stop-t_start)
    t_time = sum(t_times)
    if run == 1:
        run4.append(t_time)
    elif run == 2:
        run5.append(t_time)
    elif run == 3:
        run6.append(t_time)

def run_all():
    complete_time = perf_counter()
    # Step 1
    # run_step_1()
    #
    # # Step 2
    # run_step_2()

    # Step 3: 500 samples
    perf1 = perf_counter()
    threads = [None] * 125
    for i in range(0, 125):
        t = Thread(target=run_step_3, args=(8, 500, 1, 0))
        threads[i] = t
        t.start()
    for t in threads:
        t.join()
    run1_time = sum(run1)
    run1_time_average = run1_time / 1000
    perf1_stop = perf_counter()
    print(f"Step 3:\n" +
          f"\tRun 1: 500 samples over 1000 arrays: (Bubble Sort)\n\n " +
          f"\t\tNumber of Threads required: 125\n" +
          f"\t\tAverage Time: {run1_time_average: 0.6f}\n" +
          f"\t\tTotal Time elapsed since thread start: {(perf1_stop-perf1)/60:0.2f} min\n")

    # Step 3: 2500 samples
    perf2 = perf_counter()
    threads = [None] * 125
    for j in range(0, 125):
        t = Thread(target=run_step_3, args=(8, 2500, 2, j))
        threads[j] = t
        t.start()
    for i in range(0, len(threads)):
        threads[i].join()

    run2_time = sum(run2)
    run2_time_average = run2_time / 1000
    perf2_stop = perf_counter()
    print(f"\tRun 2: 2500 samples over 1000 arrays: (Bubble Sort)\n\n" +
          f"\t\tNumber of Threads required: 125\n" +
          f"\t\tAverage Time: {run2_time_average: 0.6f}\n" +
          f"\t\tTotal Time elapsed since thread start: {(perf2_stop-perf2)/60:0.2f} min\n")

    # Step 3: 5000 samples
    perf3 = perf_counter()
    threads = [None] * 125
    for j in range(0, 125):
        t = Thread(target=run_step_3, args=(8, 5000, 3, j))
        threads[j] = t
        t.start()
    for i in range(0, len(threads)):
        threads[i].join()

    run3_time = sum(run3)
    run3_time_average = run3_time / 1000
    perf3_stop = perf_counter()
    print(f"\tRun 3: 5000 samples over 1000 arrays: (Bubble Sort)\n\n" +
          f"\t\tNumber of Threads required: 125\n" +
          f"\t\tAverage Time: {run3_time_average: 0.6f}\n" +
          f"\t\tTotal Time elapsed since thread start: {(perf3_stop-perf3)/60:0.2f} min\n")

    # # Step 4: 500 samples
    # perf4 = perf_counter()
    # threads = [None] * 125
    # for i in range(0, 125):
    #     t = Thread(target=run_step_4, args=(8, 500, 1, 0))
    #     threads[i] = t
    #     t.start()
    # for t in threads:
    #     t.join()
    # run4_time = sum(run4)
    # run4_time_average = run1_time / 1000
    # perf4_stop = perf_counter()
    # print(f"Step 4:\n" +
    #       f"\tRun 1: 500 samples over 1000 arrays: (Selection Sort)\n\n" +
    #       f"\t\tNumber of Threads required: 125\n" +
    #       f"\t\tAverage Time: {run4_time_average: 0.6f}\n" +
    #       f"\t\tTotal Time elapsed since thread start: {(perf4_stop-perf4)/60:0.2f} min\n")
    #
    # # Step 4: 2500 samples
    # perf5 = perf_counter()
    # threads = [None] * 125
    # for j in range(0, 125):
    #     t = Thread(target=run_step_4, args=(8, 2500, 2, j))
    #     threads[j] = t
    #     t.start()
    # for i in range(0, len(threads)):
    #         threads[i].join()
    #
    # run5_time = sum(run5)
    # run5_time_average = run5_time / 1000
    # perf5_stop = perf_counter()
    # print(f"\tRun 2: 2500 samples over 1000 arrays: (Selection Sort)\n\n" +
    #       f"\t\tNumber of Threads required: 125\n" +
    #       f"\t\tAverage Time: {run5_time_average: 0.6f}\n" +
    #       f"\t\tTotal Time elapsed since thread start: {(perf5_stop-perf5)/60:0.2f} min\n")
    #
    # # Step 4: 5000 samples
    # perf6 = perf_counter()
    # threads = [None] * 125
    # for j in range(0, 125):
    #     t = Thread(target=run_step_4, args=(8, 5000, 3, j))
    #     threads[j] = t
    #     t.start()
    # for i in range(0, len(threads)):
    #         threads[i].join()
    #
    # run6_time = sum(run6)
    # run6_time_average = run6_time / 1000
    # perf6_stop = perf_counter()
    # print(f"\tRun 3: 5000 samples over 1000 arrays: (Selection Sort)\n\n" +
    #       f"\t\tNumber of Threads required: 125\n" +
    #       f"\t\tAverage Time: {run6_time_average: 0.6f}\n" +
    #       f"\t\tTotal Time elapsed since thread start: {(perf6_stop-perf6)/60:0.2f} min\n")

    # Get total time of code execution:
    complete_time_stop = perf_counter()
    print(f"Time to complete execution of all code: {complete_time_stop-complete_time}")
