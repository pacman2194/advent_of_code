package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//// PART 2

func main() {
	file, err := os.Open("day1.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var prev, curr int
	scanner.Scan()
	prev, _ = strconv.Atoi(scanner.Text())

	incr := 0
	for scanner.Scan() {
		curr, _ = strconv.Atoi(scanner.Text())
		if curr > prev {
			incr += 1
		}
		prev = curr
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
	fmt.Println(incr)
}

//// PART 1

// func main() {
// 	file, err := os.Open("day1.txt")
// 	if err != nil {
// 		fmt.Println(err)
// 		os.Exit(1)
// 	}
// 	defer file.Close()

// 	scanner := bufio.NewScanner(file)

// 	var prev, curr int
// 	scanner.Scan()
// 	prev, _ = strconv.Atoi(scanner.Text())

// 	incr := 0
// 	for scanner.Scan() {
// 		curr, _ = strconv.Atoi(scanner.Text())
// 		if curr > prev {
// 			incr += 1
// 		}
// 		prev = curr
// 	}

// 	if err := scanner.Err(); err != nil {
// 		fmt.Println(err)
// 	}
// 	fmt.Println(incr)
// }
