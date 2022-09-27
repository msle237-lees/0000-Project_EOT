#include "steps.h"
#include "../sorts/sorts.h"
#include "../create_arrs/create_arrs.h"
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */

using namespace steps;
using namespace sorts;
using namespace arrs;
using namespace std;

void step_protocols::step_1() {
	std::cout << "Enter array size for step 1 - Bubble Sort: ";
	int n;
	std::cin >> n;
	int step1[n];
	for (int i=0; i<n; i++) {
		step1[i] = rand()%10000;
	}

	std::cout << "Unsorted Array: \n";
	arrs_data::printArray(step1, n);
	std::cout << "Sorted Array: \n";
	sort::bubbleSort(step1, n);
	arrs_data::printArray(step1, n);
	std::cout << "\n";
}
void step_protocols::step_2() {
	std::cout << "Enter array size for step 2 - Selection Sort: ";
	int n;
	std::cin >> n;
	int step1[n];
	for (int i=0; i<n; i++) {
		step1[i] = rand()%10000;
	}

	std::cout << "Unsorted Array: \n";
	arrs_data::printArray(step1, n);
	std::cout << "Sorted Array: \n";
	sort::selectionSort(step1, n);
	arrs_data::printArray(step1, n);
	std::cout << "\n";
}
void step_protocols::step_3(unsigned a, unsigned n) {
	double step3_t = 0;
	std::chrono::time_point<std::chrono::system_clock> ss, se, as, ae;
	as = std::chrono::system_clock::now();
	int** step3_a = arrs_data::create2DArray(a, n);
	int i;
	for (i=0; i<a; i++) {
		ss = std::chrono::system_clock::now();
		sort::bubbleSort(step3_a[i], n);
		se = std::chrono::system_clock::now();
		std::chrono::duration<double> es = se - ss;
		step3_t += es.count();
	}
	ae = std::chrono::system_clock::now();
	std::chrono::duration<double> eas = ae - as;
	std::cout << "Step 3 - Bubble Sort - " << a << " arrays each with " << n << " elements: \n";
	std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";
	std::cout << "\t Average Execution Time: " << step3_t/a << " seconds\n\n";

	// important: clean up memory
	for (int h = 0; h < a; h++) {
		delete [] step3_a[h];
	}
	delete [] step3_a;
	step3_a = 0;
}
void step_protocols::step_4(unsigned a, unsigned n) {
  double step4_t = 0;
  std::chrono::time_point<std::chrono::system_clock> ss, se, as, ae;
  as = std::chrono::system_clock::now();
  int** step4_a = arrs_data::create2DArray(a, n);
  int i;
  for (i=0; i<a; i++) {
  	ss = std::chrono::system_clock::now();
  	sort::selectionSort(step4_a[i], n);
  	se = std::chrono::system_clock::now();
  	std::chrono::duration<double> es = se - ss;
  	step4_t += es.count();
  }
  ae = std::chrono::system_clock::now();
  std::chrono::duration<double> eas = ae - as;
  std::cout << "Step 4 - Selection Sort - " << a << " arrays each with " << n << " elements: \n";
  std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";
  std::cout << "\t Average Execution Time: " << step4_t/a << " seconds\n\n";

  // important: clean up memory
  for (int h = 0; h < a; h++) {
  	delete [] step4_a[h];
  }
  delete [] step4_a;
  step4_a = 0;
}
