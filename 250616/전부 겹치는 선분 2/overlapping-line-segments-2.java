import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[][] lines = new int[N][2];

        for (int i = 0; i < N; i++){
            int x1, x2;
            x1 = sc.nextInt();
            x2 = sc.nextInt();

            lines[i][0] = x1;
            lines[i][1] = x2;
        }

        boolean flag = false;
        for (int i = 0; i < N; i++){
            int[] records = new int[101];

            for(int j = 0; j < N; j++){

                // 하나의 선분 제외
                if (i==j){
                    continue;
                }

                for(int k = lines[j][0]; k <= lines[j][1]; k++){
                    records[k] += 1;
                }
            }

            for (int rc : records){
                if (rc >= N - 1){
                    flag = true;
                }
            }

            if (flag){
                break;
            }
        }

        if (flag){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }


    }
}