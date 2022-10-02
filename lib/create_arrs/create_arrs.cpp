// Include the necessary c++ libraries and header files
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */

// Include the necessary modules from lib folder
#include <create_arrs.h>

// using the std namespace
using namespace std;

// using the arrs namespace from the module create_arrs
using namespace arrs;

// Function to print an array
void arrs_data::printArray(int arr[], int size) {
	// Initialize i variable
	int i;

	// Output beginning bracket
	std::cout << "\t[ ";

	// for loop from 0 to size of the array
	for (i = 0; i < size; i++) {

		// Output element of array
		std::cout << arr[i] << " ";
	}

	// Output closing bracket
	std::cout << " ]" << std::endl;
}

// Function to create a 2D array (Used for steps 3 and 4)
int** arrs_data::create2DArray(unsigned height, unsigned width)
{
	// Initialize the 2D Array variable
	int** array2D = 0;

	// Initialze the 2D array elements
	array2D = new int*[height];

	// for loop from 0 to height variable (h)
	for (int h = 0; h < height; h++) {

		// the element location within 2D array is set to a new array
		array2D[h] = new int[width];

		// for loop from 0 to width variable (w)
		for (int w = 0; w < width; w++) {

			// set the 2D array element at [h][w]
			array2D[h][w] = rand()%10000;
		}
	}

	// Exit the program
  return array2D;
}
