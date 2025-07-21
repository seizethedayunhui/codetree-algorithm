import java.util.*;

public class Main {
    public static void main(String[] args) {

        // 원리 : max값을 찾아서, 그 max값에서 평균값에 미치지 못한 값들에게 max값의 일부를 떼어주는 방식.
        // 단, 평균 -max, 평균 - 해당값 중 작은 값을 더해주는 것이 key point !
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];
        int arrSum = 0;

        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
            arrSum += arr[i];
        }

        int arrAvg = (int) arrSum / N;

        boolean flag = false;

        int cnt = 0;

        // flag를 활용
        while(!flag){

            int firstMax = Integer.MIN_VALUE;

            int firstIdx = -1;

            for(int i = 0; i < N; i++){

                // first MAX값 
                if(arr[i] > firstMax){
                    firstMax = arr[i];
                    firstIdx = i;
                } 
            }


            for(int j = 0; j < N ; j++){

                if ( j != firstIdx && arr[j] < arrAvg ){

                    int amount = Math.min(Math.abs(arrAvg - arr[j]) , Math.abs(arrAvg - arr[firstIdx]));
                    cnt += amount;
                    arr[j] += amount;
                    arr[firstIdx] -= amount;
                    break; 

                }
            }

            // for(int l = 0; l < N; l++){
            //     System.out.println(arr[l]);
            // }

            // System.out.println();

            boolean sameFlag = true;

            for(int k = 0; k < N - 1; k++){
                if (arr[k] != arr[k + 1]){
                    sameFlag = false;
                    break;
                }
            }

            if (sameFlag){
                flag = true;
            }

        }

        System.out.println(cnt);
    }
}