package main

import (
	"fmt"
	"sync"
	"time"
)

const numPhilosophers = 5
const maxConcurrentEaters = 2

type Philosopher struct {
	number    int
	eatCount  int
	leftFork  *sync.Mutex
	rightFork *sync.Mutex
}

func (p *Philosopher) dine(wg *sync.WaitGroup, host chan struct{}) {
	defer wg.Done()

	for p.eatCount < 3 {
		// Request permission to eat from the host
		host <- struct{}{} // Blocking if maxConcurrentEaters is reached

		// Pick up forks (in any order)
		p.leftFork.Lock()
		p.rightFork.Lock()

		// Eat
		fmt.Printf("starting to eat %d\n", p.number)
		time.Sleep(time.Second) // Simulate eating time
		fmt.Printf("finishing eating %d\n", p.number)
		p.eatCount++

		// Put down forks
		p.rightFork.Unlock()
		p.leftFork.Unlock()

		// Release permission to eat
		<-host
	}
}

func main() {
	var wg sync.WaitGroup
	host := make(chan struct{}, maxConcurrentEaters) // Limit to maxConcurrentEaters

	// Initialize forks
	forks := make([]*sync.Mutex, numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		forks[i] = &sync.Mutex{}
	}

	// Initialize philosophers
	philosophers := make([]*Philosopher, numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		philosophers[i] = &Philosopher{
			number:    i + 1,
			leftFork:  forks[i],
			rightFork: forks[(i+1)%numPhilosophers],
		}
	}

	// Start dining
	wg.Add(numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		go philosophers[i].dine(&wg, host)
	}

	// Wait for all philosophers to finish
	wg.Wait()
}
