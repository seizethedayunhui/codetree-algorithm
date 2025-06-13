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

        for(int j = 0; j < N ; j++){
            
            // 픽하는 것의 개수 구하기
            int idxCnt = 0;
            int[] picks = new int[L];

            for (int k = 0; k < N ; k++){

                if ( j == k ){
                    continue;
                }

                if (idxCnt < L && arr[k] + 1 == arr[j]){
                    picks[idxCnt] = k;
                    arr[k] += 1; // 일단 값을 추가해줌.
                    idxCnt++;
                }
            }

            int cnt = 0;
            for(int l = 0; l < N; l++){
                if (arr[l] >= arr[j]){
                    cnt++;
                }
            }

            // H 이상인 수가 H 이상인 것을 만족하는 경우
            if ( cnt >= arr[j] && cnt >= maxCnt ){
                maxValue = Math.max(maxValue, arr[j]);
            }

            // 원래대로 돌리기
            for (int idx : picks){
                arr[idx] -= 1;
            }
        }

        System.out.print(maxValue);
        
    }
}