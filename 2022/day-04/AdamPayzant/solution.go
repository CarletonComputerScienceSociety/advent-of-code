package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ReadLines(file_path string) []string {
	dat, err := os.ReadFile(file_path)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(dat), "\n")
	if lines[0] == "" {
		lines = lines[1 : len(lines)-1]
	}
	if lines[len(lines)-1] == "" {
		lines = lines[0 : len(lines)-1]
	}

	return lines
}

func part1(input []string) int {
	res := 0

	for i := 0; i < len(input); i++ {
		div := strings.Split(input[i], ",")
		a_range := strings.Split(div[0], "-")
		b_range := strings.Split(div[1], "-")

		a_start, _ := strconv.Atoi(a_range[0])
		a_end, _ := strconv.Atoi(a_range[1])
		b_start, _ := strconv.Atoi(b_range[0])
		b_end, _ := strconv.Atoi(b_range[1])

		if (a_start <= b_start && a_end >= b_end) ||
			(b_start <= a_start && b_end >= a_end) {
			res += 1
		}
	}

	return res
}

func part2(input []string) int {
	res := 0

	for i := 0; i < len(input); i++ {
		div := strings.Split(input[i], ",")
		a_range := strings.Split(div[0], "-")
		b_range := strings.Split(div[1], "-")

		a_start, _ := strconv.Atoi(a_range[0])
		a_end, _ := strconv.Atoi(a_range[1])
		b_start, _ := strconv.Atoi(b_range[0])
		b_end, _ := strconv.Atoi(b_range[1])

		if !(a_end < b_start || a_start > b_end) {
			res += 1
		}
	}

	return res
}

func main() {
	data := ReadLines("input")

	p1 := part1(data)
	p2 := part2(data)

	fmt.Printf("Part1 = %d\n", p1)
	fmt.Printf("Part2 = %d\n", p2)
}
