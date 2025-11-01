import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] mat = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat[i][j] = sc.nextInt();
            }
        }

        int maxWidth = -1;

        // x = 행
        for (int x = 0; x < N; x++) {
            // y = 열
            for (int y = 0; y < M; y++) {

                // 사각형 크기
                for (int i = 1; i <= N - x; i++) {
                    for (int j = 1; j <= M - y; j++) {
                        boolean flag = true;

                        // 현재 (x, y)에서 i×j 사각형 검사
                        for (int k = 0; k < i; k++) {
                            for (int l = 0; l < j; l++) {
                                if (mat[x + k][y + l] < 0) {
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) break;
                        }

                        // 사각형 전체가 모두 양수일 때만 갱신
                        if (flag) {
                            int area = i * j;
                            maxWidth = Math.max(maxWidth, area);
                        }
                    }
                }
            }
        }

        System.out.println(maxWidth);
    }
}
