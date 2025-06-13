import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] bombs = new int[N];
        int bomb;

        for (int i = 0; i < N ; i++){
            bomb = sc.nextInt();
            bombs[i] = bomb;
        }

        // 큰값을 구하기 위한 기본값
        int maxBombNum = 0;
        double maxCnt = Double.NEGATIVE_INFINITY;
        boolean flag = false;

        // 전체 터진 것을 메모하는 배열
        int[] records = new int[N];

        // j = 기준이 되는 인덱스
        for(int j = 0; j < N ; j++ ){

            // 터지는 경우를 메모
            for (int k = 0; k < N ; k++){

                if (bombs[j]==bombs[k] && Math.abs(j-k) <= K){
                    flag = true;
                    // 터진 것을 기록함. 
                    records[k] = 1;
                }
            }

                
        }


        if (flag){

            for (int l = 0; l < N ; l++){

                if (records[l] == 1) {
                    int cnt = 0;
                    for (int m = 0; m < N ; m++){
                        if ( records[m] == 1 && bombs[l] == bombs[m] ){
                                cnt += 1;
                        
                    }
                    // System.out.println(bombs[l] + "일 때 cnt : " + cnt + ", 현재 최댓값: " + maxCnt );
                    if (cnt > maxCnt ) {
                        maxBombNum = bombs[l];
                        maxCnt = cnt;
                    } else if ( cnt == maxCnt ){
                            maxBombNum = Math.max(maxBombNum, bombs[l]);
                            maxCnt = cnt;
                    }

                        
                    }
                }
                
            }

        System.out.print(maxBombNum);
        
        }
    }
}