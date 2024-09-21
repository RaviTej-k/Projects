package application;

public class QuickAlgo3M {
	public  void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Finding the pivot using median of three technique
            int pivot = medianOfThree(arr, low, high);
            // Partition the array around the pivot
            int pi = partition(arr, low, high, pivot);
            // Recursively sort elements before and after partition
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static int medianOfThree(int[] arr, int low, int high) {
        int mid = low + (high - low) / 2;
        if (arr[low] > arr[mid])
            swap(arr, low, mid);
        if (arr[mid] > arr[high])
            swap(arr, mid, high);
        if (arr[low] > arr[mid])
            swap(arr, low, mid);
        return arr[mid];
    }

    public static int partition(int[] arr, int low, int high, int pivot) {
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
