#include <sorts.h>
#include <iostream>

using namespace sorts;

//Swap function
void sort::swap(int *xp, int *yp)
{
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

// A function to implement bubble sort
void sort::bubbleSort(int arr[], int n)
{
  int i, j;
  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        sort::swap(&arr[j], &arr[j + 1]);
      }
    }
  }
}

// A function to implement selection sort
void sort::selectionSort(int arr[], int n) {
	int i, j, min_idx;
	for (i = 0; i < n-1; i++) {
		min_idx = i;
		for (j = i+1; j < n; j++) {
			if (arr[j] < arr[min_idx]) {
				min_idx = j;
			}
			if(min_idx!=i) {
				sort::swap(&arr[min_idx], &arr[i]);
			}
		}
	}
}
