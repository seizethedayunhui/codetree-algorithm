import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int Q = sc.nextInt();

        int[][] mat = new int[N][M];
        int[][] temp = new int[N][M];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                int element = sc.nextInt();
                mat[i][j] = element;
                temp[i][j] = element;
            }
        }

        for(int wind = 0; wind < Q; wind++){
            int startX = sc.nextInt();
            int startY = sc.nextInt();
            int endX = sc.nextInt();
            int endY = sc.nextInt();
            int tempElement;

            // 방향이동 후 temp 배열에 저장
            // 오른쪽 방향
            tempElement = mat[startX-1][endY-1];
            for(int i = endY-1; i >= startY; i--){
                temp[startX-1][i] = mat[startX-1][i-1];
            }
            // 아래 방향
            temp[startX][endY-1] = tempElement;
            tempElement = mat[endX-1][endY-1];
            for(int j = endX-1; j > startX; j--){
                temp[j][endY-1] = mat[j-1][endY-1];
            }
            // 왼쪽 방향
            temp[endX-1][endY-2] = tempElement;
            tempElement = mat[endX-1][startY-1];
            for(int k = startY-1; k < endY-1; k++ ){
                temp[endX-1][k] = mat[endX-1][k+1];
            }
            // 위쪽 방향
            temp[endX-2][startY-1] = tempElement;
            for(int l = startX-1; l < endX -1; l++){
                temp[l][startY-1] = mat[l+1][startY-1];
            }

            int[][] direc = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

            // mat 배열 갱신
            for(int x = startX - 1; x < endX; x++){
                for(int y = startY - 1; y < endY; y++){

                    int currentSum = temp[x][y];
                    int cnt = 1;
                    for(int i = 0; i < 4; i++){

                        int nx = x + direc[i][0];
                        int ny = y + direc[i][1];
                        // 범위 확인
                        if ( nx >= 0 && nx < N && ny >= 0 && ny < M ){
                            cnt += 1;
                            currentSum += temp[nx][ny];
                        }
                    }

                    int value = currentSum / cnt;

                    mat[x][y] = value;
                }
            }
        }

        for(int x = 0; x < N; x++){
            for(int y = 0; y < M; y++){
                System.out.print(mat[x][y] + " ");
            }
            System.out.println();
        }

    }
}