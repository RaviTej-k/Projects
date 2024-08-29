package main

import (
	"fmt"
)

// Swap function swaps the elements at index i and i+1
func Swap(slice []int, i int) {
	slice[i], slice[i+1] = slice[i+1], slice[i]
}

// BubbleSort function sorts the slice using the Bubble Sort algorithm
func BubbleSort(slice []int) {
	n := len(slice)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if slice[j] > slice[j+1] {
				Swap(slice, j)
			}
		}
	}
}

func main() {
	// Prompt the user to enter up to 10 integers
	var input int
	var numbers []int
	fmt.Println("Enter up to 10 integers. Type 'x' to stop early.")

	for i := 0; i < 10; i++ {
		fmt.Printf("Enter integer %d: ", i+1)
		_, err := fmt.Scan(&input)
		if err != nil {
			break // Stop if the user enters a non-integer (e.g., 'x')
		}
		numbers = append(numbers, input)
	}

	// Sort the slice using Bubble Sort
	BubbleSort(numbers)

	// Print the sorted integers
	fmt.Println("Sorted integers:")
	for _, num := range numbers {
		fmt.Print(num, " ")
	}
}
