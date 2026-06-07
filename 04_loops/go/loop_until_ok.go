package main

import "fmt"

func main() {
	var input string

	for {
		fmt.Print("Type ok: ")
		fmt.Scanln(&input)

		if input == "ok" {
			fmt.Println("OK!")
			break
		}

		fmt.Println("Try again.")
	}
}
