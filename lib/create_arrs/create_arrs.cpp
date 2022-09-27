#include <create_arrs.h>
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */

using namespace arrs;
using namespace std;

// Function to print an array
void arrs_data::printArray(int arr[], int size) {
	int i;
	std::cout << "\t[ ";
	for (i = 0; i < size; i++) {
		std::cout << arr[i] << " ";
	}
	std::cout << " ]";
	std::cout << std::endl;
}

int** arrs_data::create2DArray(unsigned height, unsigned width)
{
	int** array2D = 0;
	array2D = new int*[height];
	for (int h = 0; h < height; h++) {
		array2D[h] = new int[width];
		for (int w = 0; w < width; w++) {
			array2D[h][w] = rand()%10000;
		}
	}
  return array2D;
}
