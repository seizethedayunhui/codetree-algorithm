import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 격자의 크기
        int M = sc.nextInt(); // 연속해서 나와야하는 수의 개수

        int[][] mat = new int[N][N];

        // mat 입력 받음. 
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        int cnt = 0;

        // 사실상 크기는 1*M or M*1임 -> 2가지로 나눠서?

        for(int row = 0; row < N; row++){

            int currentCnt = 1; // 0번을 원소로 넣음. 
            int currentElement = mat[row][0];

            // 연속해서 M개 이상 나와야함. 
            for(int col = 1; col < N; col++){

                // M개 보다 많이 나온 경우 cnt + 1
                // 이전 원소랑 같은 경우
                if (mat[row][col] == currentElement){
                    currentCnt += 1;
                } else {
                    currentCnt = 1;
                }

                if (currentCnt >= M){
                    cnt += 1;
                    break;
                }

                currentElement = mat[row][col];
            }
        }

    

        for (int col = 0; col < N; col++){
            int currentCnt = 1;
            int currentElement = mat[0][col];

            for(int row = 1; row < N; row++){


                if(mat[row][col] == currentElement){
                    currentCnt += 1;
                } else{
                    currentCnt = 1;
                }

                if(currentCnt >= M){
                    cnt += 1;
                    break;
                }
                
                currentElement = mat[row][col];
            }
        }
        
        System.out.println(cnt);
    }
}