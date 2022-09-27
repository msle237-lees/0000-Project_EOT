#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include "../lib/Steps/steps.h"

using namespace steps;

int main()
{
  step_protocols::step_1();
	step_protocols::step_2();
	std::chrono::time_point<std::chrono::system_clock> as, ae;
	as = std::chrono::system_clock::now();
	step_protocols::step_3(1000, 500);
	step_protocols::step_3(1000, 2500);
	step_protocols::step_3(1000, 5000);
	step_protocols::step_4(1000, 500);
	step_protocols::step_4(1000, 2500);
	step_protocols::step_4(1000, 5000);
	ae = std::chrono::system_clock::now();
	std::chrono::duration<double> eas = ae - as;
	std::cout << "\t Total Execution Time: " << eas.count() << " seconds\n";
	return 0;
}
