import java.util.*;

public class Main {

    // 범위 확인 함수
    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    // 다음 배열 결정 후 반환해주는 함수
    public static int[] nextElementsFunc(int direcIdx, int[] prevElements, int prevElement){
        int[] nextElements = { 0, 0, 0, 0};

        // 좌우 이동의 경우, 좌우만 반전시키면 됨.
        // 상하는 고정

        // 상하 이동의 경우, 상하만 반전시키면 됨.
        // 좌우는 고정
        for(int i = 0; i < 4; i++){
            if(i == direcIdx){
                nextElements[i] = 7 - prevElement;
            } else if ((i+2) % 4 == direcIdx){
                nextElements[i] = prevElement;
            } else {
                nextElements[i] = prevElements[i];
            }
        }

        // System.out.println("다음배열, R D L U");
        // for(int i = 0; i < 4; i++){
        //     System.out.print(nextElements[i] + " ");
        // }
        // System.out.println();
        // System.out.println();

        return nextElements;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int r = sc.nextInt() - 1;
        int c = sc.nextInt() - 1;

        String[] directions = new String[M];
        for(int k = 0; k < M; k++){
            directions[k] = sc.next();
        }

        // 모두 0으로 초기화
        int[][] mat = new int[N][N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                mat[i][j] = 0;
            }
        }

        // R D L R 방향 이동
        int[] dx = { 0, 1, 0, -1};
        int[] dy = { 1, 0, -1, 0};

        // 초기에 R D L R 방향 이동 시 그곳의 값
        int[] nextElements = { 3, 2, 4, 5};
        // 이전의 값
        int currentElement = 6;
        mat[r][c] = 6;

        int nr;
        int nc;
        int direcIdx;
        int nextElement;
        String nextDirec;
        
        for(int l = 0; l < M; l++){

            nr = r;
            nc = c;

            nextDirec = directions[l];

            if (nextDirec.equals("R")){
                direcIdx = 0;
            } else if (nextDirec.equals("D")){
                direcIdx = 1;
            } else if (nextDirec.equals("L")){
                direcIdx = 2;
            } else {
                direcIdx = 3;
            }

            nr += dx[direcIdx];
            nc += dy[direcIdx];

            if (inRange(nr, nc, N)){

                // 다음 값 설정
                nextElement = nextElements[direcIdx];
                
                nextElements = nextElementsFunc(direcIdx, nextElements, currentElement);

                // 나중에 r,c 값 갱신 필수
                r = nr;
                c = nc;
                currentElement = nextElement;
                mat[r][c] = currentElement;

            } else {
                continue;
            }


            // for(int x = 0; x < N; x++){
            //     for(int y = 0; y < N; y++){
            //         System.out.print(mat[x][y] + " ");
            //     }
            //     System.out.println();
            // }
            // System.out.println();
        }

        int cnt = 0;
        for(int x = 0; x < N; x++){
            for(int y = 0; y < N; y++){
                cnt += mat[x][y];
            }
        }

        System.out.println(cnt);

    }
}