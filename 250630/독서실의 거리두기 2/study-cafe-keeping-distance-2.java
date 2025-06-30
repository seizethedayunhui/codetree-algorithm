import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        String input = sc.next();

        for(int i = 0; i < N; i++){
            arr[i] = input.charAt(i) - '0';
        }

        int maxDistance = Integer.MIN_VALUE;

        for(int i = 0; i < N; i++){

            int newMember = i;

            if (arr[newMember] == 1){
                continue;
            }

            arr[newMember] = 1;

            int startIdx =  0; // 거리를 재기 위한 시작 인덱스
            boolean flag = false;

            int minDistance = Integer.MAX_VALUE;

            for(int j = 0; j < N; j++){

                if (arr[j] == 1){
                    if (!flag){
                        startIdx = j;
                        flag = true;
                    } else {
                        int currentDistance = Math.abs(j-startIdx);
                        startIdx = j;
                        minDistance = Math.min(minDistance, currentDistance);
                    }
                }

                // System.out.println(minDistance);
            }

            maxDistance = Math.max(maxDistance, minDistance);

            arr[newMember] = 0;

        }

        System.out.println(maxDistance);
    }
}