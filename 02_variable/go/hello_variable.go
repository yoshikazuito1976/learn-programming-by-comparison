package main

import "fmt"

func main() {
	name := "yoshikazu"

	fmt.Println(name)
	fmt.Println("name")
	fmt.Println("Hello, " + name)

	fmt.Printf("Hello, %s\n", name)
	fmt.Println(fmt.Sprintf("Hello, %s", name))

	firstName, lastName := "yoshikazu", "ito"

	fmt.Println(firstName)
	fmt.Println(lastName)
	fmt.Printf("%s %s\n", lastName, firstName)
}
