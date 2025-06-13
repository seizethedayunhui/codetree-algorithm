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
        double max_bomb_num = Double.NEGATIVE_INFINITY;
        double max_cnt = Double.NEGATIVE_INFINITY;

        // j = 기준이 되는 인덱스
        for(int j = 0; j < N ; j++ ){

            // bombs 배열을 전부 돌면서 같은 정수의 폭탄이 K 이내에 있는지 확인
            boolean flag = false;
            int cnt = 0;
            for (int k = 0; k < N ; k++){

                if (bombs[j]==bombs[k] && Math.abs(j-k) <= K){
                    flag = true;
                    cnt += 1;
                }
            }

            // flag와 횟수 비교
            if (flag && cnt > max_cnt ) {
                max_bomb_num = bombs[j];
                max_cnt = cnt;
            } else if ( cnt == max_cnt ){
                max_bomb_num = Math.max(max_bomb_num, bombs[j]);
                max_cnt = cnt;
            }
   
        }

        System.out.print((int)max_bomb_num);
        
    }
}