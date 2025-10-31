import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] mat = new int[N][N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        // 가능한 K의 값 : N - 1
        int maxCnt = 0;
        int maxIncome = 0;     

        for(int x = 0 ; x < N; x++){
            for(int y = 0 ; y < N; y++){
                // 점마다 계산
                for(int k = N-1; k > 0; k--){

                    int expense = (k * k) + (k+1)*(k+1); // 비용 먼저 계산
                    int income = 0;
                    int currentCnt = 0;



                    for( int row = 0; row < 2 * k + 1; row++){

                        if (row <= k){
                            for(int col = (-1) * row ; col < row + 1; col++){

                                if ( (x - k + row) < 0 || (x + row - k) >= N || y + col < 0 || y + col >= N ){
                                    continue;
                                } else {
                                    currentCnt += mat[x + (row-k)][y + col];
                                    income += (mat[x + (row-k)][y + col] * M);   
                                    //System.out.println("K: " + k + ", (x, y): " +(x + (row-k)) +", " + (y + col) + " cnt: " + currentCnt);                            
                                }
                            }

                        } else {
                            for(int col = (-1) * (row % k) ; col < (row % k) + 1; col++){

                                if ( (x - k + row) < 0 || (x + row - k) >= N || y + col < 0 || y + col >= N ){
                                    continue;
                                } else {
                                    currentCnt += mat[x + (row-k)][y + col];
                                    income += (mat[x + (row-k)][y + col] * M);   
                                    //System.out.println("K: " + k + ", (x, y): " +(x + (row-k)) +", " + (y + col) + " cnt: " + currentCnt);                            
                                }
                            }                            
                        }

                    }     

                    

                    if((income > expense) && currentCnt >= maxCnt ){

                        maxCnt = currentCnt;
                        //System.out.println("K: " + k + ", (x, y): " + x  +", " + y + " cnt: " + currentCnt + ", amount:" + (income - expense));
                    }

                }
            }
        }

        System.out.println(maxCnt);
    
    }
}