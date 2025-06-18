import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();

        int[][] jumps = { {x, y}, {y, x} };

        int minDis = Integer.MAX_VALUE;
        for(int i = 0; i < 2; i++){

            int currentDis = 0;
            boolean jumpFlag = false;

            int direct = 0;

            if (jumps[i][0] < A){

                direct = -1;

            } else {

                direct = 1;
            }; 

            for (int j = A; j < B; ){
                
                if (jumps[i][0] == j && !jumpFlag ){
                    j = jumps[i][1];
                    jumpFlag = true;

                    if (direct < 0){
                        direct = 1;
                    }
                } else {
                    j += direct;
                    currentDis += 1;
                }
            }

            minDis = Math.min(minDis, currentDis);
        }
        
        System.out.println(minDis);
    }
}