import java.util.*;

public class Main {
    // quickSort with JAVA
    static int partition(int[] arr, int low, int high){

        int idx = low-1;

        for(int i = low; i < high; i++){
            if(arr[i] < arr[high]){
                idx += 1;
                int temp = arr[idx];
                arr[idx] = arr[i];
                arr[i] = temp;
            }
        }
        
        int temp = arr[idx+1];
        arr[idx+1] = arr[high];
        arr[high] = temp;

        return idx + 1;
    }

    static void quickSort(int[] arr, int low, int high){

        if (low < high){
            int pos = partition(arr, low, high);

            quickSort(arr, low, pos-1);
            quickSort(arr, pos+1, high);
        }
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        quickSort(arr, 0, n-1);

        for( int element : arr ){
            System.out.print(element + " ");
        }


    }
}