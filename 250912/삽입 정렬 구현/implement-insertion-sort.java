import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
        }

        for(int j = 1; j < N; j++){
            int k = j-1;
            int key = arr[j];

            while ( k >= 0 && arr[k] > key){
                arr[k+1] = arr[k];
                k--;
            }
            arr[k+1] = key; 
        }
        
        for(int elem : arr){
             System.out.print(elem+ " ");
        } 

    }
}