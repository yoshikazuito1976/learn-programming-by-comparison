package main

import "fmt"

func main() {
	items := []string{"apple", "banana", "orange"}

	for i, item := range items {
		fmt.Println(i, item)
	}
}