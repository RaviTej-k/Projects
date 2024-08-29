package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"io/ioutil"
	"os"
)

// Define a struct to hold the API response
type ExchangeRates struct {
	Rates map[string]float64 `json:"conversion_rates"`
	Base  string             `json:"base_code"`
}

func main() {
	// Replace with your API URL and key
	// apiKey := "e38745e457f51715d0efbd53"
	var baseCurrency, targetCurrency string
	var amount float64
	fmt.Println("Enter the base currency : ")
	fmt.Scan(&baseCurrency)
	fmt.Println("Enter the amount: ")
	fmt.Scan(&amount)
	fmt.Println("Enter the target currency : ")
	fmt.Scan(&targetCurrency)	

	//  API request URL
	url := fmt.Sprintf("https://v6.exchangerate-api.com/v6/e38745e457f51715d0efbd53/latest/%s",baseCurrency)
	
	// Make the HTTP request
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	defer resp.Body.Close()
	
	// Read the entire response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		os.Exit(1)
	}
	
	// Decode the JSON response into the struct
	var rates ExchangeRates
	if err := json.Unmarshal(body, &rates); err != nil {
		fmt.Println("Error decoding JSON:", err)
		os.Exit(1)
	}

	// Check if the base currency exists in the rates map
	conversionRate, exists := rates.Rates[baseCurrency]
	if !exists {
		fmt.Printf("Error: Rate for %s not found.\n", baseCurrency)
		os.Exit(1)
	}
	// Check if the target currency exists in the rates map
	conversionRate, exists = rates.Rates[targetCurrency]
	if !exists {
		fmt.Printf("Error: Rate for %s not found.\n", targetCurrency)
		os.Exit(1)
	}

	convertedAmount := amount * conversionRate
	fmt.Printf("%.2f %s is equivalent to %.2f %s\n", amount, baseCurrency, convertedAmount, targetCurrency)
}
