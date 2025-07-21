import java.util.*;

public class Main {
    public static void main(String[] args) {

        // 원리 : max1에서 max2를 뺸값은 max1 && max2가 아닌 값으로 옮겨주는 것을 반복하는 방식. 
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
        }

        boolean flag = false;

        int cnt = 0;

        // flag를 활용
        while(!flag){

            int firstMax = Integer.MIN_VALUE;
            int secondMax = Integer.MIN_VALUE;

            int firstIdx = -1;
            int secondIdx = -1;

            for(int i = 0; i < N; i++){

                // first MAX값과 second MAX 값을 구해줌. 
                if(arr[i] > firstMax && arr[i] > secondMax){

                    secondMax = firstMax;
                    firstMax = arr[i];

                    secondIdx = firstIdx;
                    firstIdx = i;

                } else if (arr[i] < firstMax  && arr[i] > secondMax ){
                    secondMax = arr[i];
                    secondIdx = i;
                }
            }

            // System.out.println("현재 max1, max2 = " + firstMax + ", " + secondMax);

            for(int j = 0; j < N ; j++){
                if ( j != firstIdx && j != secondIdx && arr[j] != firstMax && arr[j] != secondMax ){
                    arr[j] += Math.abs(arr[firstIdx] - arr[secondIdx]);
                    arr[firstIdx] -= Math.abs(arr[firstIdx] - arr[secondIdx]);
                    cnt += Math.abs(firstMax - secondMax);
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