import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int L = sc.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N ; i++){
            arr[i] = sc.nextInt();
        }

        int maxCnt = 0;
        int maxValue = 0;

        for(int j = 1; j <= 100 ; j++){
            
            // 픽하는 것의 개수 구하기
            int idxCnt = 0;
            int[] picks = new int[L];

            for (int k = 0; k < N ; k++){


                if (idxCnt < L && arr[k] + 1 == j ){
                    picks[idxCnt] = k;
                    arr[k] += 1; // 일단 값을 추가해줌.
                    idxCnt++;
                }
            }

            int cnt = 0;
            for(int l = 0; l < N; l++){
                if (arr[l] >= j ){
                    cnt++;
                }
            }
 
            // H 이상인 수가 H 이상인 것을 만족하는 경우 중에서 큰 값.
            if ( cnt >= j ){
                maxValue = Math.max(maxValue, j);            
            }

            // 원래대로 돌리기
            // iter 값 사용하지 마라... 제발
            for (int n = 0; n < idxCnt ; n++){
                arr[picks[n]] -= 1;
            }

        }

        System.out.print(maxValue);
        
    }
}