import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String[] info = sc.next().split("");
        int[] information = new int[N];

        for (int i = 0; i < N; i++){
            information[i] = Integer.parseInt(info[i]);
        }

        int maxDistance = Integer.MIN_VALUE;
        int start;
        int end;

        // 가장 긴 거리를 구함. 
        for(int i = 0; i < N; i++){

            if (information[i] == 1){
                continue;
            }

            information[i] = 1;

            boolean flag = false;
            int startPoint = 0;
            int minDistance = Integer.MAX_VALUE;

            for (int j = 0; j < N; j++){
                if (information[j] == 1){

                    if (!flag){
                        // 가장 처음 1인 idx를 찾기 위한 조건임. 
                        startPoint = j;
                        flag = true;

                    } else {

                        int currentDistance = j - startPoint;
                        startPoint = j;

                        minDistance = Math.min(minDistance, currentDistance);
                    }
                    
                }
            }

            // System.out.println(minDistance);
            information[i] = 0;

            maxDistance = Math.max(maxDistance, minDistance);
            
        }

        System.out.println(maxDistance);
    }
}