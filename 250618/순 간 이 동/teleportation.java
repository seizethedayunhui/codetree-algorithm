import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();

        int[][] jumps = { {x, y}, {y, x} };

        int minDis = Math.abs(A-B);

        for(int i = 0; i < 2; i++){

            boolean jumpFlag = false;

            int direct = 0;

            if (jumps[i][0] < A){

                direct = -1;

            } else {

                direct = 1;
            }; 


            int j = A;
            int currentDis = 0;

            while( j != B) {
                
                if (jumps[i][0] == j && !jumpFlag ){
                    j = jumps[i][1];
                    jumpFlag = true;

                    // 이동한 위치에 따라서 이동 방향 조정
                    if ( j > B ){
                        direct = -1;
                    } else {
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