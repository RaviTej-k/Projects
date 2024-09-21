package application;

public class HeapSortAlgo {
		public void sort(int arr[])
		{
			int n = arr.length;

			// Building heap (rearrange array)
			for (int i = n / 2 - 1; i >= 0; i--)
				heapify(arr, n, i);

			// One by one extracting an element from heap
			for (int i = n - 1; i >= 0; i--) {
				// Move the current root to end
				int temp = arr[0];
				arr[0] = arr[i];
				arr[i] = temp;

				// calling the max heapify on the reduced heap
				heapify(arr, i, 0);
			}
		}

		
		void heapify(int arr[], int n, int i)
		{
			int largest = i; 
			int l = 2 * i + 1; 
			int r = 2 * i + 2; 

			// If left child is larger than root
			if (l < n && arr[l] > arr[largest])
				largest = l;

			// If right child is larger than largest so far
			if (r < n && arr[r] > arr[largest])
				largest = r;

			// If largest is not root
			if (largest != i) {
				int swap = arr[i];
				arr[i] = arr[largest];
				arr[largest] = swap;

				// Recursively heapify the affected sub-tree
				heapify(arr, n, largest);
			}
		}
	
}
