// Import necessary c++ libraries
#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <fstream> /* ofstream */

// Import custom module from lib folder
#include "../lib/Steps/steps.h"

// Using custom module class
using namespace steps;

int main()
{
  // Call Step 1 Function from custom module class
  step_protocols::step_1();

  // Call Step 2 Function from custom module class
	step_protocols::step_2();

  // Initialize the performance counter variables
	std::chrono::time_point<std::chrono::system_clock> as, ae;

  // Take the system time and store
	as = std::chrono::system_clock::now();

  // Call Step 3 Function with 1000 arrays with 500 elements
	double step3_500 = step_protocols::step_3(1000, 500);

  // Call Step 3 Function with 1000 arrays with 2500 elements
	double step3_2500 = step_protocols::step_3(1000, 2500);

  // Call Step 3 Function with 1000 arrays with 5000 elements
	double step3_5000 = step_protocols::step_3(1000, 5000);

  // Call Step 4 Function with 1000 arrays with 500 elements
	double step4_500 = step_protocols::step_4(1000, 500);

  // Call Step 4 Function with 1000 arrays with 2500 elements
	double step4_2500 = step_protocols::step_4(1000, 2500);

  // Call Step 4 Function with 1000 arrays with 5000 elements
	double step4_5000 = step_protocols::step_4(1000, 5000);

  // Take the system time and store
	ae = std::chrono::system_clock::now();

  // Find the difference between end time and start time
	std::chrono::duration<double> eas = ae - as;

  // Output total execution time with unit seconds
	std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";

  // Exit program
	return 0;
}
