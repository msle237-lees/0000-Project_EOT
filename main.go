package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func create_2d_array(x, y int) [][]int {
	var arr [][]int
	for i := 0; i < x; i++ {
		var temp []int
		for j := 0; j < y; j++ {
			temp = append(temp, rand.Intn(10000))
		}
		arr = append(arr, temp)
	}
	return arr
}

func bubble_sort(arr []int) []int {
	for i := 0; i < len(arr)-1; i++ {
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

func selection_sort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		var minIdx = i
		for j := i; j < len(arr); j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	}
	return arr
}

func main() {
	// For Step 5: open and write to csv file for each step below
	current_time := time.Now()
	file_name := "doc/data_" + current_time.Format("2006-01-02_15-04-05") + ".csv"
	file, err := os.Create(file_name)
	if err != nil {
		log.Fatalf("failed creating file: %s", err)
	}
	writer := csv.NewWriter(file)
	fmt.Println("Storing data in file: ", file_name)

	// Step 1: Bubble Sort array of size n, n = user inputted number
	var in string
	var n int
	fmt.Print("Enter size of array (n): ")
	fmt.Scanln(&in)
	n, _ = strconv.Atoi(in)
	arr := create_2d_array(1, n)
	start_time := time.Now()
	fmt.Println("Array unsorted: ", arr[0])
	bubble_sort(arr[0])
	fmt.Println("Array sorted: ", arr[0])
	ex_time_step_1 := time.Since(start_time)
	fmt.Println("Step 1: with array of size ", in, ", total execution time is: ", ex_time_step_1)
	fmt.Println("")

	// Step 2: Selection Sort array of size n, n = user inputted number
	fmt.Print("Enter size of array (n): ")
	fmt.Scanln(&in)
	n, _ = strconv.Atoi(in)
	arr = create_2d_array(1, n)
	start_time = time.Now()
	fmt.Println("Array unsorted: ", arr[0])
	selection_sort(arr[0])
	fmt.Println("Array sorted: ", arr[0])
	ex_time_step_2 := time.Since(start_time)
	fmt.Println("Step 2: with array of size ", in, ", total execution time is: ", ex_time_step_2)
	fmt.Println("")

	// Step 3: Bubble Sort 1000 arrays with sizes 500, 2500, 5000 elements
	// 500 elements
	arr = create_2d_array(1000, 500)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		bubble_sort(arr[i])
	}
	ex_time_step_3_a := time.Since(start_time) / 1000
	fmt.Println("Step 3: With 1000 arrays with size 500, average execution time is: ", ex_time_step_3_a)

	// 2500 elements
	arr = create_2d_array(1000, 2500)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		bubble_sort(arr[i])
	}
	ex_time_step_3_b := time.Since(start_time) / 1000
	fmt.Println("Step 3: With 1000 array with size 2500, average execution time is: ", ex_time_step_3_b)

	// 5000 elements
	arr = create_2d_array(1000, 5000)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		bubble_sort(arr[i])
	}
	ex_time_step_3_c := time.Since(start_time) / 1000
	fmt.Println("Step 3: With 1000 array with size 5000, average execution time is: ", ex_time_step_3_c)

	// Step 4: Selection Sort 1000 arrays with sizes 500, 2500, 5000 elements
	// 500 elements
	arr = create_2d_array(1000, 500)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		selection_sort(arr[i])
	}
	ex_time_step_4_a := time.Since(start_time) / 1000
	fmt.Println("Step 4: With 1000 arrays with size 500, average execution time is: ", ex_time_step_4_a)

	// 2500 elements
	arr = create_2d_array(1000, 2500)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		selection_sort(arr[i])
	}
	ex_time_step_4_b := time.Since(start_time) / 1000
	fmt.Println("Step 4: With 1000 array with size 2500, average execution time is: ", ex_time_step_4_b)

	// 5000 elements
	arr = create_2d_array(1000, 5000)
	start_time = time.Now()
	for i := 0; i < len(arr); i++ {
		selection_sort(arr[i])
	}
	ex_time_step_4_c := time.Since(start_time) / 1000
	fmt.Println("Step 4: With 1000 array with size 5000, average execution time is: ", ex_time_step_4_c)

	var data_list [][]string
	data_list = append(data_list, []string{"Step", "Elements", "Execution Time"})
	data_list = append(data_list, []string{"3", "500", ex_time_step_3_a.String()})
	data_list = append(data_list, []string{" ", "2500", ex_time_step_3_b.String()})
	data_list = append(data_list, []string{" ", "5000", ex_time_step_3_c.String()})
	data_list = append(data_list, []string{"4", "500", ex_time_step_4_a.String()})
	data_list = append(data_list, []string{" ", "2500", ex_time_step_4_b.String()})
	data_list = append(data_list, []string{" ", "5000", ex_time_step_4_c.String()})
	for _, value := range data_list {
		_ = writer.Write(value)
	}
	writer.Flush()
	file.Close()
}
