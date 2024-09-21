package application;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Random;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main extends Application {
	//ArrayList contaning the time taken values is declared
	public static ArrayList<Integer> vl = new ArrayList<Integer>();
	
	DecimalFormat df = new DecimalFormat("#.##");
    CategoryAxis xAxis;
    NumberAxis yAxis;
    BarChart<String, Number> barChart;
    XYChart.Series<String, Number> series;
    
    @Override
    public void start(Stage stage) {
    	// Creating a label, text field, and button for input parameter
        Label nameLabel = new Label("Enter the size of array:");
        TextField nameTextField = new TextField();
        Button submitButton = new Button("Submit");
        submitButton.getStyleClass().add("button");
        
     // Event handler for the submit button
        submitButton.setOnAction(event -> {
            String number = nameTextField.getText();
            try {
	            int n = Integer.parseInt(number);
	            processInputNumber(n);
	        } 
            catch (NumberFormatException e) {
	            System.out.println("Invalid input! Please enter a valid number.");
	        }
        });
        
        // Creating the x-axis and y-axis
        xAxis = new CategoryAxis();
        yAxis = new NumberAxis();

        // Creating the bar chart
        barChart = new BarChart<>(xAxis, yAxis);
        barChart.setTitle("Comparison of Sorting Algorithm");

        xAxis.setLabel("Sorting Algorithm");
        yAxis.setLabel("Time in mili seconds");

        // Defining the data series
        series = new XYChart.Series<>();
        series.setName("Time Complexity");

        // Adding data points to the series
        series.getData().add(new XYChart.Data<>("Merge", vl.get(0)));
        series.getData().add(new XYChart.Data<>("Heap", vl.get(1)));
        series.getData().add(new XYChart.Data<>("Quick", vl.get(2)));
        series.getData().add(new XYChart.Data<>("Quick 3 Median", vl.get(3)));
        series.getData().add(new XYChart.Data<>("Insertion", vl.get(4)));
        series.getData().add(new XYChart.Data<>("Selection", vl.get(5)));
        series.getData().add(new XYChart.Data<>("Bubble", vl.get(6)));

        // Adding the series to the chart
        barChart.getData().add(series);

        // Creating a vertical box layout to hold the controls
        VBox vbox = new VBox(10);
        vbox.setPadding(new Insets(20));
        vbox.getChildren().addAll(nameLabel, nameTextField, submitButton,  barChart);


        // Creating the scene and set it to the stage
        Scene scene = new Scene(vbox, 600, 400);
        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
        stage.setScene(scene);
        stage.setTitle("DAA Project GUI");
        stage.show();
    }
    
    // Method to process the input number
    private void processInputNumber(int n) {
        //Random number generated and assigned to array of size n
    	Random rand = new Random();
		int[] arr = new int[n];
		for(int i=0 ; i<n;i++) {
			arr[i] = rand.nextInt(100);
		}
		//Arraylist being cleared So new values can be updated
		vl.clear();
		
		//To Display input array in console
		//System.out.println("Initial Array:");
		//printArray(arr);
		
		//Call all Sorting Algorithm methods
		mergeSort(arr);
		heapSort(arr);
		quickSortReg(arr);
		quickSortMedian(arr);
		insertionSort(arr);
		selectionSort(arr);
		bubbleSort(arr);
		
		//method to update chart with new values from Sorting Algorithms
		updateChart();
    }
    
    // Method to update the chart with new data based on the input number
    private void updateChart() {
        // Clear existing data
        series.getData().clear();
        // Adding new data points 
        series.getData().add(new XYChart.Data<>("Merge", vl.get(0)));
        series.getData().add(new XYChart.Data<>("Heap", vl.get(1)));
        series.getData().add(new XYChart.Data<>("Quick", vl.get(2)));
        series.getData().add(new XYChart.Data<>("Quick 3 Median", vl.get(3)));
        series.getData().add(new XYChart.Data<>("Insertion", vl.get(4)));
        series.getData().add(new XYChart.Data<>("Selection", vl.get(5)));
        series.getData().add(new XYChart.Data<>("Bubble", vl.get(6)));
    }

    public static void main(String[] args) {
    	//Initial ArrayList being assigned as 0
    	for(int i=0;i<=6;i++) {
    		vl.add(0);
    	}
    	//GUI Function
        launch(args);
        
    }
    
    //Method to execute Merge Sort
    public static void mergeSort(int arr[]) {
    	//Duplicated Array to execute Sorting
		int[] marr = new int[arr.length];
		System.arraycopy(arr, 0, marr, 0, arr.length);
		//Declaring a class object
		MergeSortAlgo al = new MergeSortAlgo();
		long start = System.nanoTime();
		al.sort(marr,0,marr.length-1);
		long end = System.nanoTime();		
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(0, (int) tm);
		//System.out.println("Sorted Array (Merge Sort):");
		//printArray(marr);
		System.out.println("Execution of Merge Sort has taken :" + tm +" ms");
	}
    
    //Method to execute Heap Sort
    public static void heapSort(int arr[]) {
    	//Duplicated Array to execute Sorting
		int[] harr = new int[arr.length];
		System.arraycopy(arr, 0, harr, 0, arr.length);
		//Declaring a class object
		HeapSortAlgo al = new HeapSortAlgo();
		long start = System.nanoTime();
		al.sort(harr);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(1, (int) tm);
		//System.out.println("Sorted Array (Heap Sort):");
		//printArray(harr);
		System.out.println("Execution of Heap Sort has taken :" + tm +" ms");
	}
    
  //Method to execute Insertion Sort
	public static void insertionSort(int arr[]) {
		//Duplicated Array to execute Sorting
		int[] iarr = new int[arr.length];
		System.arraycopy(arr, 0, iarr, 0, arr.length);
		//Declaring a class object
		InsertionAlgo al = new InsertionAlgo();
		long start = System.nanoTime();
		al.sort(iarr);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(4, (int) tm);
		//System.out.println("Sorted Array (Insertion Sort):");
		//printArray(iarr);
		System.out.println("Execution of Insertion Sort has taken :" + tm +" ms");
	}
	
	//Method to execute Selection Sort
	public static void selectionSort(int arr[]) {
		//Duplicated Array to execute Sorting
		int[] sarr = new int[arr.length];
		System.arraycopy(arr, 0, sarr, 0, arr.length);
		//Declaring a class object
		SelectionAlgo al = new SelectionAlgo();
		long start = System.nanoTime();
		al.sort(sarr);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(5, (int) tm);
		//System.out.println("Sorted Array (Selection Sort):");
		//printArray(sarr);
		System.out.println("Execution of Selection Sort has taken :" + tm +" ms");
	}
	//Method to execute Bubble Sort
	public static void bubbleSort(int arr[]) {
		//Duplicated Array to execute Sorting
		int[] barr = new int[arr.length];
		System.arraycopy(arr, 0, barr, 0, arr.length);
		//Declaring a class object
		SelectionAlgo al = new SelectionAlgo();
		long start = System.nanoTime();
		al.sort(barr);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(6, (int) tm);
		//System.out.println("Sorted Array (Bubble Sort):");
		//printArray(barr);
		System.out.println("Execution of Bubble Sort has taken :" + tm +" ms");
	}
	
	//Method to execute Quick Sort
	public static void quickSortReg(int arr[]) {
		//Duplicated Array to execute Sorting
		int[] qarr = new int[arr.length];
		System.arraycopy(arr, 0, qarr, 0, arr.length);
		//Declaring a class object
		QuickAlgoReg al = new QuickAlgoReg();
		long start = System.nanoTime();
		al.quickSort(qarr,0,qarr.length-1);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(2, (int) tm);
		//System.out.println("Sorted Array (Quick Sort):");
		//printArray(qarr);
		System.out.println("Execution of Quick Sort has taken :" + tm +" ms");
	}
	
	//Method to execute Quick Sort 3Median
	public static void quickSortMedian(int arr[]) {
		//Duplicated Array to execute Sorting
		int[] qmarr = new int[arr.length];
		System.arraycopy(arr, 0, qmarr, 0, arr.length);
		//Declaring a class object
		QuickAlgo3M al = new QuickAlgo3M();
		long start = System.nanoTime();
		al.quickSort(qmarr,0,qmarr.length-1);
		long end = System.nanoTime();
		long diff = end - start;
		float tm =roundOff(diff);
		//Updating ArrayList with new value
		vl.add(3, (int) tm);
		//System.out.println("Sorted Array (Quick Sort 3 Median):");
		//printArray(qmarr);
		System.out.println("Execution of Quick Sort(3 Median) has taken :" + tm +" ms");
	}
	
	//Method to Print elements of the array
    public static void printArray(int arr[]){
        int n = arr.length;
        System.out.print("[");
        for (int i = 0; i < n; ++i)
            System.out.print( arr[i] + "  ");
        System.out.print("]");
        System.out.println();
    }
    
    //Method to convert ns to ms
    public static float roundOff(long num) {
    	double milliseconds = (double) num / 1000000; 
    	BigDecimal bd = new BigDecimal(milliseconds);
    	bd = bd.setScale(2, BigDecimal.ROUND_HALF_UP);
    	float finalval = bd.floatValue();
		return finalval;	   
    }
}
