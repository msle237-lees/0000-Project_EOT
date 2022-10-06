// include the necessary c++ libraries and header files
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */

// include the necessary header files from the lib folder
#include "steps.h"
#include "../sorts/sorts.h"
#include "../create_arrs/create_arrs.h"

// using the default std namespace
using namespace std;

// using the included namespaces from the custom header files
using namespace steps;
using namespace sorts;
using namespace arrs;

/*
	Function namespace: step_protocols
	Function name: step_1
	Arguments: None
	Process:
		- Take input from the user asking for array size (n)
		- Create array of size n
		- Populate each element of the array with a random number from 0 to 10,000
		- Print the unsorted array
		- Call the bubbleSort function from the namespace sort
		- Print the sorted array
*/
void step_protocols::step_1() {
	// Ask for input from the user
	std::cout << "Enter array size for step 1 - Bubble Sort: ";

	// Define the size of the array as n
	int n;

	// Take in user input and store in n
	std::cin >> n;

	// Create the array (list) of size n
	int step1[n];

	// Loop through array and populate each element with a random number 0 to 10,000
	for (int i=0; i<n; i++) {
		step1[i] = rand()%10000;
	}

	// Output unsorted array
	std::cout << "Unsorted Array: \n";
	arrs_data::printArray(step1, n);

	// Sort the array
	sort::bubbleSort(step1, n);

	// Output sorted array
	std::cout << "Sorted Array: \n";
	arrs_data::printArray(step1, n);
	std::cout << "\n";

}

/*
	Function namespace: step_protocols
	Function name: step_2
	Arguments: None
	Process:
		- Take input from the user asking for array size (n)
		- Create array of size n
		- Populate each element of the array with a random number from 0 to 10,000
		- Print the unsorted array
		- Call the selectionSort function from the namespace sort
		- Print the sorted array
*/
void step_protocols::step_2() {
	// Ask for input from the user
	std::cout << "Enter array size for step 1 - Bubble Sort: ";

	// Define the size of the array as n
	int n;

	// Take in user input and store in n
	std::cin >> n;

	// Create the array (list) of size n
	int step2[n];

	// Loop through array and populate each element with a random number 0 to 10,000
	for (int i=0; i<n; i++) {
		step2[i] = rand()%10000;
	}

	// Output unsorted array
	std::cout << "Unsorted Array: \n";
	arrs_data::printArray(step2, n);

	// Sort the array
	sort::selectionSort(step2, n);

	// Output sorted array
	std::cout << "Sorted Array: \n";
	arrs_data::printArray(step2, n);
	std::cout << "\n";

}

/*
	Function namespace: step_protocols
	Function name: step_3
	Arguments: unsigned integers a, n
	Process:
		- Call create2DArray function from arrs namespace with number of arrays (a) and number of elements (n) as arguments
		- Above function returns two dimensional array, with size (a, n)
		- Loop through this arrays first dimension and sort all the the second dimension array with the bubbleSort function
		- Time each run and add the times to the total time variable
		- Print out total execution time and the average run time for each array
*/
double step_protocols::step_3(unsigned a, unsigned n) {
	// Create the total time variable and set it to 0
	double step3_t = 0;

	// Define the time point variables used later
	std::chrono::time_point<std::chrono::system_clock> ss, se, as, ae;

	// Take the total execution time start time
	as = std::chrono::system_clock::now();

	// Create the 2 Dimensional array with arguments a and n
	int** step3_a = arrs_data::create2DArray(a, n);

	// Loop through the array from 0 to a
	int i;
	for (i=0; i<a; i++) {
		// Take the run time start time
		ss = std::chrono::system_clock::now();

		// Call the bubble sort function with the arguments each inner array with size n
		sort::bubbleSort(step3_a[i], n);

		// Take the run end time
		se = std::chrono::system_clock::now();

		// Determine how long the run took and add to the total time
		std::chrono::duration<double> es = se - ss;
		step3_t += es.count();
	}

	// Take the end total execution time
	ae = std::chrono::system_clock::now();

	// Calculate the total execution time
	std::chrono::duration<double> eas = ae - as;

	// Print the total execution time and average execution time
	std::cout << "Step 3 - Bubble Sort - " << a << " arrays each with " << n << " elements: \n";
	std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";
	std::cout << "\t Average Execution Time: " << step3_t/a << " seconds\n\n";

	// important: clean up memory
	for (int h = 0; h < a; h++) {
		delete [] step3_a[h];
	}
	delete [] step3_a;
	step3_a = 0;

	return step3_t/a;
}

/*
	Function namespace: step_protocols
	Function name: step_3
	Arguments: unsigned integers a, n
	Process:
		- Call create2DArray function from arrs namespace with number of arrays (a) and number of elements (n) as arguments
		- Above function returns two dimensional array, with size (a, n)
		- Loop through this arrays first dimension and sort all the the second dimension array with the selectionSort function
		- Time each run and add the times to the total time variable
		- Print out total execution time and the average run time for each array
*/
double step_protocols::step_4(unsigned a, unsigned n) {
	// Create the total time variable and set it to 0
	double step4_t = 0;

	// Define the time point variables used later
	std::chrono::time_point<std::chrono::system_clock> ss, se, as, ae;

	// Take the total execution time start time
	as = std::chrono::system_clock::now();

	// Create the 2 Dimensional array with arguments a and n
	int** step4_a = arrs_data::create2DArray(a, n);

	// Loop through the array from 0 to a
	int i;
	for (i=0; i<a; i++) {
		// Take the run time start time
		ss = std::chrono::system_clock::now();

		// Call the selection sort function with the arguments of each inner array with size n
		sort::selectionSort(step4_a[i], n);

		// Take the run end time
		se = std::chrono::system_clock::now();

		// Determine how long the run took and add to the total time
		std::chrono::duration<double> es = se - ss;
		step4_t += es.count();
	}

	// Take the end total execution time
	ae = std::chrono::system_clock::now();

	// Calculate the total execution time
	std::chrono::duration<double> eas = ae - as;

	// Print the total execution time and average execution time
	std::cout << "Step 4 - Bubble Sort - " << a << " arrays each with " << n << " elements: \n";
	std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";
	std::cout << "\t Average Execution Time: " << step4_t/a << " seconds\n\n";

	// important: clean up memory
	for (int h = 0; h < a; h++) {
		delete [] step4_a[h];
	}
	delete [] step4_a;
	step4_a = 0;

	return step4_t/a;
}
