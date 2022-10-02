// Include the necessary c++ library
#include <iostream>

// include the necessary header files
#include <sorts.h>

// using the sorts namespace from the sorts header file
using namespace sorts;

//Swap function
void sort::swap(int *xp, int *yp)
{
  // Initialze a temp value to store xp variable (*xp)
  int temp = *xp;

  // set the temp value *xp equal to *yp
  *xp = *yp;

  // set the temp value *yp equal to temp value
  *yp = temp;
}

// A function to implement bubble sort
void sort::bubbleSort(int arr[], int n)
{
  // Initialize i and j variables
  int i, j;

  // for loop from 0 to n -1
  for (i = 0; i < n - 1; i++) {

    // for loop from j to n - i - 1
    for (j = 0; j < n - i - 1; j++) {

      // If array[j] is less than the next value (array[j+1])
      if (arr[j] > arr[j + 1]) {

        // Call the swap function to swap the values locations
        sort::swap(&arr[j], &arr[j + 1]);
      }
    }
  }
}

// A function to implement selection sort
void sort::selectionSort(int arr[], int n) {
  // Initialze variables j, j, and min_idx (minimum index)
	int i, j, min_idx;

  // for loop from 0 to n - 1
	for (i = 0; i < n-1; i++) {

    // set min_idx to the value of i
		min_idx = i;

    // for loop from i+1 to n
		for (j = i+1; j < n; j++) {

      // test if arr[j] is less than arr[min_idx]
			if (arr[j] < arr[min_idx]) {

        // if so then set min_idx to equal j
				min_idx = j;
			}

      // test if min_idx is not equal to i
			if(min_idx!=i) {

        // if so then call the swap function to swap the values locations
				sort::swap(&arr[min_idx], &arr[i]);
			}
		}
	}
}
