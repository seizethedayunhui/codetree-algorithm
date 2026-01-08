import java.util.*;

public class Main {
    
    public static int N;
    public static int[][] mat;
    public static boolean[][] visited;

    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };
    
    // 폭탄 개수 세기
    public static int blockCnt;

    public static boolean inRange(int x, int y){
        return ((x >= 0 && x < N) && ( y >= 0 && y < N));
    }

    public static boolean canGo(int x, int y, int K){
        return (inRange(x,y) && (mat[x][y] == K) && (!visited[x][y]));
    }

    public static void dfs(int x, int y, int K){

        visited[x][y] = true;
        blockCnt++;

        int nx, ny;

        for(int i = 0; i < 4; i++){
            nx = x + dx[i];
            ny = y + dy[i];

            if (canGo(nx, ny, K)) {
                dfs(nx, ny, K);
            }
        }
    }


    public static int maxBlockCnt = 0;
    public static int bombCnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        mat = new int[N][N];
        visited = new boolean[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }

        int k;

        for(k = 1; k < 101; k++){
            for(int x = 0; x < N; x++){
                for(int y = 0; y < N; y++){
                    if (canGo(x, y, k)){
                        blockCnt = 0;
                        dfs(x, y, k);

                        if (blockCnt >= 4){
                            bombCnt++;
                        }

                        maxBlockCnt = Math.max(maxBlockCnt, blockCnt);
                    }
                }
            }
        }

        System.out.println(bombCnt + " " + maxBlockCnt);
    }
}