package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	filePath := "C:/Users/hxzzm/OneDrive/Documents/Git/Advent-of-Code-2023/practice/2022/2/input.txt"
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var p1x, p1y int
	p1Map := map[string]int{
		"up":   -1,
		"down": 1,
	}

	var p2x, p2y, p2a int

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		if len(strings.TrimSpace(line)) == 0 {
			continue
		}

		parts := strings.Split(line, " ")
		s := parts[0]
		intValue, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Println("Error parsing integer:", err)
			continue
		}

		if s == "up" || s == "down" {
			p1y += intValue * p1Map[s]
		} else {
			p1x += intValue
		}

		if s == "up" || s == "down" {
			p2a += intValue * p1Map[s]
		} else {
			p2x += intValue
			p2y += p2a * intValue
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println("Part One:", p1y*p1x)
	fmt.Println("Part Two:", p2x*p2y)
}
