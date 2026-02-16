import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[][] mat = new int[N][N];
        int[][] dpMin = new int[N][N];
        int[][] dpMax = new int[N][N];


        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        dpMin[0][0] = mat[0][0];
        dpMax[0][0] = mat[0][0];

        // 0번째 행 채우기
        for(int c=1; c < N; c++){
            dpMin[0][c] = Math.min(dpMin[0][c-1], mat[0][c]);
            dpMax[0][c] = Math.max(dpMax[0][c-1], mat[0][c]);
        }

        // 0번째 열 채우기
        for(int r=1; r < N; r++){
            dpMin[r][0] = Math.min(dpMin[r-1][0], mat[r][0]);
            dpMax[r][0] = Math.max(dpMax[r-1][0], mat[r][0]);            
        }

        int minFromTop, maxFromTop, minFromLeft, maxFromLeft, fromTop, fromLeft;

        // 나머지 채우기
        for(int x = 1; x < N; x++){
            for(int y = 1; y < N; y++){

                // 위에서 오는 값
                minFromTop = Math.min(dpMin[x-1][y], mat[x][y]);
                maxFromTop = Math.max(dpMax[x-1][y], mat[x][y]);    
                fromTop = Math.abs(minFromTop-maxFromTop);

                // 왼쪽에서 오는 값
                minFromLeft = Math.min(dpMin[x][y-1], mat[x][y]);
                maxFromLeft = Math.max(dpMax[x][y-1], mat[x][y]);    
                fromLeft = Math.abs(minFromLeft-maxFromLeft); 

                if (fromTop < fromLeft){
                    dpMin[x][y] = minFromTop;
                    dpMax[x][y] = maxFromTop;
                } else{
                    dpMin[x][y] = minFromLeft;
                    dpMax[x][y] = maxFromLeft;                    
                }          
            }
        }

        // for(int i = 0; i < N; i++){
        //     for(int j = 0; j < N; j++){
        //         System.out.print(dpMin[i][j] + ", " + dpMax[i][j] + " ");
        //     }
        //     System.out.println();
        // }

        int ans = Math.abs(dpMax[N-1][N-1] - dpMin[N-1][N-1]);

        System.out.println(ans);
    }
}