import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] birds = new int[N];

        for(int i = 0; i < N; i++){
            birds[i] = -1;
        }

        int cnt = 0;
        for(int i = 0; i < N; i++){
            int bird = sc.nextInt();
            int location = sc.nextInt();

            // 움직임이 발생되기 전
            if (birds[bird -1] < 0){
                birds[bird -1] = location;
            } else if (birds[bird - 1] != location){
                cnt += 1;
                birds[bird - 1] = location;
            }
        }

        System.out.println(cnt);
    }
}