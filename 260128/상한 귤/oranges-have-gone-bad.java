import java.util.*;

public class Main {

    public static int N, K;
    public static int[][] mat;
    public static Queue<int[]> q = new ArrayDeque<>();

    public static boolean[][] visited;
    public static int[][] time;

    public static boolean inRange(int x, int y){
        return ((x >= 0 && x < N) && (y >= 0 && y < N));
    }

    public static boolean canGo(int x, int y){
        return (inRange(x, y) && !visited[x][y] && (mat[x][y] == 1));
    }

    public static void bfs(){

        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };

        while (!q.isEmpty()){

            int[] c = q.poll();
            int cx = c[0];
            int cy = c[1];
            int cTime = time[cx][cy];

            for(int i = 0; i < 4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (canGo(nx, ny)){

                    visited[nx][ny] = true;
                    time[nx][ny] = cTime + 1;
                    int[] n = {nx, ny};
                    q.offer(n);
                    mat[nx][ny] = 2;
                }
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        mat = new int[N][N];
        visited = new boolean[N][N];
        time = new int[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int e = sc.nextInt();

                mat[i][j] = e;

                if (e == 2){
                    int[] element = {i, j};
                    q.offer(element);
                    time[i][j] = 0;
                } else if ( e == 1 ){
                    time[i][j] = -2;
                } else {
                    time[i][j] = -1;
                }
            }
        }

        bfs();

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                System.out.print(time[i][j] + " ");
            }
            System.out.println();
        }

    }
}