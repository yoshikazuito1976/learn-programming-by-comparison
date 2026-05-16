package main

import "fmt"

func main() {
	username := "student"
	password := "linux"

	if username == "student" && password == "linux" {
		fmt.Println("ログイン成功")
	} else {
		fmt.Println("ログイン失敗")
	}
}
