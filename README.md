# 0001-Project_EOT
End of Term Project for CSE 2300: Discrete Structures

## For the professor to execute ##
1. Open the `code` folder
2. Open the `build` folder
3. Open the `Release` folder
4. Double click the `Project_EOT` executable
5. After the code has completed press enter to close the terminal

## All code can be found within the code folder in the `main.cpp` file ##

## Requirements: ##
1. Write a computer program that prompts the user for a number, creates an array for that number of random integers, and then uses the bubble sort to order the array. The program should print out the array prior to the call to the sorting algorithm and afterwards. You can write the program in either Java, C++, C#, or whatever language you are most comfortable in. DO NOT USE AN API FROM THE LANGUAGE LIBRARY. WRITE THE PROGRAM TO PERFORM THE SORT.
2. Repeat 1 but use selection sort this time. AGAIN, WRITE OUT THE PROGRAM FOR THE SELECTION SORT. DO NOT USE THE LANGUAGE LIBRARY.
3. Write a computer program that prompts the user for one number, n for the number of items in the array to sort, and create and sort 1000 different arrays of this size timing the run to get an average time to sort an array of this size. Then do the following:
	* Initiate a variable running_time to 0
	* Create a for loop that iterates 1000 times
	* In the body of the loop,
	* Create an array of n random integers
	* Get the time and set this to start_time (notice the sort is started after each array is built. You want to time the sort process only). You will have to figure out what the appropriate command is in the programming language you are using to find the time (IMPORTANT: DO NOT START THE TIMER UNTIL AFTER THE ARRAY IS CREATED).
	* Use bubble sort to sort the array
	* Get the time and set this to end_time. Subtract start_time from end_time and add the result to total_time
	* Once the program has run, note
	* The number of items sorted
	* The average running time for each array (total_time / 1000)
	* Repeat the process using 500, 2500, and 5000 as the size of the array.
4. Repeat 3 using selection sort.
5. You now have 6 data points (the averages from the three array sizes for the two sort algorithms). Create a spreadsheet showing the results of 3 and 4 and create a graph to graphically represent the information. Show both sort algorithms on the same graph for comparison.
6. Write a one page document explaining the results, bearing in mind that both algorithms have a complexity of O(n^2) and what you know about complexity analysis. Use your knowledge of complexity analysis to explain your results.

## Report: ##
Can be found within `doc` folder under the name `0001-Project_EOT.docx`.

## Excel Spreadsheet showing data: ##
Can be found within the `doc` folder under the name `Data_Points_Over_10_Runs.xlsx`.

## Submission Documents: ##
1. Program code for 1 
2. Program code for 2 
3. Program code used in 3 and the results of the three program runs 
4. Program code used in 4 and the results of the three program runs
5. The spreadsheet created in 5 
6. The report. In the report, say which machine you ran the experiments on (type of processor, RAM, etc). Explain your experiment and why you feel you received the results you observed.
