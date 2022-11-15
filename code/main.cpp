#include <iostream>
#include <stdlib.h>
#include <chrono>

void printArray(int arr[], int size) {
    int i;
    std::cout << "\t[";
    for (i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << "]" << std::endl;
}

int** create2DArray(unsigned height, unsigned width) {
    int** array2D = 0;
    array2D = new int*[height];

    for (int h = 0; h < height; h++) {
        array2D[h] = new int[width];
        for (int w=0; w < width; w++) {
            array2D[h][w] = rand() % 10000;
        }
    }
    return array2D;
}

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

void step1() {
    std::cout << "Enter array size for step 1 - Bubble Sort: ";
    int n = 10;
    std::cin >> n;
    if (n <= 0) {
        std::cout << "Invalid array size" << std::endl;
        return;
    }
    int* step_1 = create2DArray(1, n)[0];
    std::cout << "Array before sorting: ";
    printArray(step_1, n);
    std::cout << "Sorting..." << std::endl;
    bubbleSort(step_1, n);
    std::cout << "Array after sorting: ";
    printArray(step_1, n);
}

void step2() {
    std::cout << "Enter array size for step 2 - Selection Sort: ";
    int n = 10;
    std::cin >> n;
    if (n <= 0) {
        std::cout << "Invalid array size" << std::endl;
        return;
    }
    int* step_2 = create2DArray(1, n)[0];
    std::cout << "Array before sorting: ";
    printArray(step_2, n);
    std::cout << "Sorting..." << std::endl;
    selectionSort(step_2, n);
    std::cout << "Array after sorting: ";
    printArray(step_2, n);
}

void step3(int a, int n) {
    double step_3_time = 0;
    std::chrono::time_point<std::chrono::system_clock> all_start, all_end, individual_start, individual_end;
    all_start = std::chrono::system_clock::now();
    int** step_3 = create2DArray(a, n);
    for (int i = 0; i < a; i++) {
        individual_start = std::chrono::system_clock::now();
        bubbleSort(step_3[i], n);
        individual_end = std::chrono::system_clock::now();
        std::chrono::duration<double> elapsed_seconds = individual_end - individual_start;
        step_3_time += elapsed_seconds.count();
    }
    all_end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = all_end - all_start;
    std::cout << "Step 3 - Bubble Sort with " << a << " arrays of size " << n << " elements: " << std::endl;
    std::cout << "\tTotal time: " << elapsed_seconds.count() << "s" << std::endl;
    std::cout << "\tIndividual time: " << step_3_time/a << "s" << std::endl;
}

void step4(int a, int n) {
    double step_4_time = 0;
    std::chrono::time_point<std::chrono::system_clock> all_start, all_end, individual_start, individual_end;
    all_start = std::chrono::system_clock::now();
    int** step_4 = create2DArray(a, n);
    for (int i = 0; i < a; i++) {
        individual_start = std::chrono::system_clock::now();
        bubbleSort(step_4[i], n);
        individual_end = std::chrono::system_clock::now();
        std::chrono::duration<double> elapsed_seconds = individual_end - individual_start;
        step_4_time += elapsed_seconds.count();
    }
    all_end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = all_end - all_start;
    std::cout << "Step 4 - Selection Sort with " << a << " arrays of size " << n << " elements: " << std::endl;
    std::cout << "\tTotal time: " << elapsed_seconds.count() << "s" << std::endl;
    std::cout << "\tIndividual time: " << step_4_time/a << "s" << std::endl;
}

int main(int, char**) {
    step1();
    step2();
    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();
    step3(1000, 500);
    step3(1000, 2500);
    step3(1000, 5000);
    step4(1000, 500);
    step4(1000, 2500);
    step4(1000, 5000);
    end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "Total time: " << elapsed_seconds.count() << "s" << std::endl;
    return 0;
}
