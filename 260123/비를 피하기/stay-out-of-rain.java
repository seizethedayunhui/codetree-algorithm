import java.util.*;

public class Main {

    public static int N;
    public static int H;
    public static int M;
    
    public static int[][] mat, avoidRain;
    public static Queue<int[]> peopleLoc = new ArrayDeque<>();

    public static boolean inRange(int x, int y){
        return ((x>=0 && x < N) && (y>= 0 && y < N));
    }

    public static boolean canGo(int x, int y, boolean[][] visited){
        return ((inRange(x, y)) && (mat[x][y] != 1) && (!visited[x][y]));
    }


    public static void bfs(){

        int x, y;
        int path;

        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };

        while (!peopleLoc.isEmpty()){

            int[] element = peopleLoc.poll();
            Queue<int[]> q = new ArrayDeque<>();
            boolean[][] visited = new boolean[N][N];
            int[][] step = new int[N][N];
            
            q.offer(element);
            x = element[0];
            y = element[1];
            path = -1;

            while (!q.isEmpty()){
                int[] element2 = q.poll();
                int cx = element2[0];
                int cy = element2[1];

                if (mat[cx][cy] == 3){
                    path = step[cx][cy];
                    break;
                }

                for(int d = 0; d < 4; d++){
                    int nx = cx + dx[d];
                    int ny = cy + dy[d];

                    if (canGo(nx, ny, visited)){
                        visited[nx][ny] = true;
                        step[nx][ny] = step[cx][cy] + 1;
                        int[] ne = {nx, ny};
                        q.offer(ne);
                    }
                }
            }

            avoidRain[x][y] = path;
            q.clear();

        }
    }


    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        H = sc.nextInt();
        M = sc.nextInt();

        mat = new int[N][N];
        avoidRain = new int[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int e = sc.nextInt();
                mat[i][j] = e;

                if (e==2){
                    int[] e2 = {i, j};
                    peopleLoc.offer(e2);
                }
            }
        }

        bfs();

        for(int i2 = 0; i2 < N; i2++){
            for(int j2 = 0; j2 < N; j2++){
                System.out.print(avoidRain[i2][j2] + " ");
            }
            System.out.println();
        }
        
    }
}