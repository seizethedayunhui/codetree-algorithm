import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 행
        int M = sc.nextInt(); // 열
        int Q = sc.nextInt(); // 회전 횟수

        int[][] mat = new int[N][M];
        int[][] temp = new int[N][M];

        // 초기 입력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat[i][j] = sc.nextInt();
                temp[i][j] = mat[i][j];
            }
        }

        // Q번 회전 수행
        for (int wind = 0; wind < Q; wind++) {
            int startX = sc.nextInt();
            int startY = sc.nextInt();
            int endX = sc.nextInt();
            int endY = sc.nextInt();

            // 인덱스 0 기반 변환
            startX--; startY--;
            endX--; endY--;

            // ---------- ① 테두리 회전 ----------
            // 오른쪽 이동
            int tempElement = mat[startX][endY];
            for (int i = endY; i > startY; i--) {
                temp[startX][i] = mat[startX][i - 1];
            }

            // 아래쪽 이동
            temp[startX + 1][endY] = tempElement;
            tempElement = mat[endX][endY];
            for (int i = endX; i > startX + 1; i--) {
                temp[i][endY] = mat[i - 1][endY];
            }

            // 왼쪽 이동
            temp[endX][endY - 1] = tempElement;
            tempElement = mat[endX][startY];
            for (int i = startY; i < endY - 1; i++) {
                temp[endX][i] = mat[endX][i + 1];
            }

            // 위쪽 이동
            temp[endX - 1][startY] = tempElement;
            for (int i = startX; i < endX - 1; i++) {
                temp[i][startY] = mat[i + 1][startY];
            }

            // ---------- ② 회전 결과 temp → mat 복사 ----------
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    mat[i][j] = temp[i][j];
                }
            }

            // ---------- ③ 평균 계산 및 mat 갱신 ----------
            int[][] direc = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

            for (int x = startX; x <= endX; x++) {
                for (int y = startY; y <= endY; y++) {
                    int currentSum = temp[x][y];
                    int cnt = 1;

                    for (int i = 0; i < 4; i++) {
                        int nx = x + direc[i][0];
                        int ny = y + direc[i][1];

                        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                            currentSum += temp[nx][ny];
                            cnt++;
                        }
                    }

                    mat[x][y] = currentSum / cnt;
                }
            }

            // 평균 계산 후 temp 갱신
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    temp[i][j] = mat[i][j];
                }
            }
        }

        // ---------- ④ 출력 ----------
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}
