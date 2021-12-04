package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

//// PART 2

func main() {
	// open file
	file, err := os.Open("day2.txt")

	// check for error opening file
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// close file at exit
	defer file.Close()

	// create scanner to read file
	scanner := bufio.NewScanner(file)

	// setup main variables
	// var depths []int
	// var horizontals []int
	var depths int
	var horizontals int
	var aim int

	// iterate over each line
	for scanner.Scan() {
		// split line
		line := strings.Split(scanner.Text(), " ")

		// get value for distance
		val, _ := strconv.Atoi(line[1])

		// switch statement for directions
		switch line[0] {

		// forward is only horizontal direction, always positive
		case "forward":
			horizontals += val
			depths += aim * val

		// up is negative depth value
		case "up":
			aim -= val

		// down is positive depth value
		case "down":
			aim += val
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println(horizontals * depths)
}

//// PART 1

// func main() {
// 	// open file
// 	file, err := os.Open("day2.txt")

// 	// check for error opening file
// 	if err != nil {
// 		fmt.Println(err)
// 		os.Exit(1)
// 	}

// 	// close file at exit
// 	defer file.Close()

// 	// create scanner to read file
// 	scanner := bufio.NewScanner(file)

// 	// setup main variables
// 	// var depths []int
// 	// var horizontals []int
// 	var depths int
// 	var horizontals int

// 	// iterate over each line
// 	for scanner.Scan() {
// 		// split line
// 		line := strings.Split(scanner.Text(), " ")

// 		// get value for distance
// 		val, _ := strconv.Atoi(line[1])

// 		// switch statement for directions
// 		switch line[0] {

// 		// forward is only horizontal direction, always positive
// 		case "forward":
// 			horizontals += val

// 		// up is negative depth value
// 		case "up":
// 			depths -= val

// 		// down is positive depth value
// 		case "down":
// 			depths += val
// 		}
// 	}

// 	if err := scanner.Err(); err != nil {
// 		fmt.Println(err)
// 	}

// 	fmt.Println(horizontals * depths)
// }
