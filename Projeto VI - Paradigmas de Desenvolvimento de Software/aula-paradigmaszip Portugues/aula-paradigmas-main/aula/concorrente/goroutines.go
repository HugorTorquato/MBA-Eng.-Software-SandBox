package main

import (
	"fmt"
	"time"
)

func trabalho(nome string) {
	fmt.Println(nome, "iniciou")
	time.Sleep(2 * time.Second)
	fmt.Println(nome, "finalizou")
}

// Iniciar os metodos de forma paralela
// cada go rotine vai chamar trabalho e depois terminar

func main(){
	go trabalho("Goroutine 1")
	go trabalho("Goroutine 2")

	time.Sleep(3*time.Second)
	fmt.Println("Todos os trabalhos foram finalizados")
}
