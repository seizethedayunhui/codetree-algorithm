import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] birds = new int[11];

        for(int i = 0; i < 11; i++){
            birds[i] = -1;
        }

        int cnt = 0;
        for(int i = 0; i < N; i++){
            int bird = sc.nextInt();
            int location = sc.nextInt();

            // 움직임이 발생되기 전
            if (birds[bird] < 0){
                birds[bird] = location;
            } else if (birds[bird] != location){
                cnt += 1;
                birds[bird] = location;
            }
        }

        System.out.println(cnt);
    }
}