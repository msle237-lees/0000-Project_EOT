from time import sleep, perf_counter
from multiprocessing import Pool, Process
import random
import sys


class main:
    def __init__(self):
        self.runs = [[], [], [], [], [], []]
        self.processes = []
        self.times = []

    def bubbleSort(self, arr):
        swap = True
        iter = 0
        while swap:
            swap = False
            for i in range(len(arr) - iter - 1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swap = True
            iter += 1

    def selectionSort(self, arr, s):
        for i in range(s):
            min = i
            for j in range(i+1, s):
                if arr[j] < arr[min]:
                    min = j
            (arr[i], arr[min]) = (arr[min], arr[i])

    def step_1(self):
        n = int(input("Enter number of elements in array for step 1: "))
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        print("Unsorted Array: ")
        print("     " + str(l))
        t_start = perf_counter()
        self.bubbleSort(l)
        t_stop = perf_counter()
        print("Sorted Array: ")
        print("     " + str(l))
        print(f"Elapsed Time for step 1: {t_stop-t_start: 0.6f}")
        return t_stop-t_start

    def step_2(self):
        n = int(input("Enter number of elements in array for step 2: "))
        l = []
        for i in range(n):
            l.append(random.randint(0, 10000))
        print("Unsorted Array: ")
        print("     " + str(l))
        t_start = perf_counter()
        self.selectionSort(l, n)
        t_stop = perf_counter()
        print("Sorted Array: ")
        print("     " + str(l))
        print(f"Elapsed Time for step 2: {t_stop-t_start: 0.6f}")
        return t_stop-t_start

    def create_arrays(self, n, i):
        l = []
        sl = []
        for a in range(i):
            for b in range(n):
                sl.append(random.randint(0, 10000))
            l.append(sl)
        return l

    def step_3(self, arr, a):
        for i in range(len(arr)):
            t_start = perf_counter()
            self.bubbleSort(arr[i])
            t_end = perf_counter()
            tt = t_end - t_start
            self.times.append(tt)
        self.runs[a].append((sum(self.times)) / len(arr))

    def step_4(self):
        pass

    def run(self):
        self.step_1()
        self.step_2()

        # Step 3: 1000 arrays, 500 samples each
        tt = perf_counter()
        processors = []
        for i in range(20):
            l = self.create_arrays(500, 50)
            processors.append(Process(target=self.step_3, args=(l,0,)))
            processors[i].start()
        for i in range(20):
            processors[i].join()

        te = perf_counter()

        print(f"Total Execution Time: {(te-tt)/60}")

        # Step 3: 1000 arrays, 2500 samples each
        tt = perf_counter()
        processors = []
        for i in range(20):
            l = self.create_arrays(2500, 50)
            processors.append(Process(target=self.step_3, args=(l,1,)))
            processors[i].start()
        for i in range(20):
            processors[i].join()

        te = perf_counter()

        print(f"Total Execution Time: {(te-tt)/60}\n" +
              f"Average Time: {self.runs}")
