import java.util.*;

public class Main {

    public static int N, K;
    public static boolean[][] mat;
    public static boolean[][] visited;

    public static ArrayList<Integer> pointX = new ArrayList<>();
    public static ArrayList<Integer> pointY = new ArrayList<>();

    public static Queue<Integer> xQueue = new ArrayDeque<>();
    public static Queue<Integer> yQueue = new ArrayDeque<>();

    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };

    public static boolean inRange(int x, int y){
        return ((x >= 0 && x < N) && (y >= 0 && y < N));
    }

    public static boolean canGo(int x, int y){
        return (inRange(x, y) && mat[x][y] && !visited[x][y]);
    }

    public static int bfs(int x, int y){

        int cnt = 1;
        visited[x][y] = true;
        xQueue.offer(x);
        yQueue.offer(y);

        while( !xQueue.isEmpty() && !yQueue.isEmpty() ){
            int currentX = xQueue.poll();
            int currentY = yQueue.poll();

            int nx, ny;

            for(int i = 0; i < 4; i++){
                nx = currentX + dx[i];
                ny = currentY + dy[i];

                if (canGo(nx, ny)){
                    cnt++;
                    visited[nx][ny] = true;
                    xQueue.offer(nx);
                    yQueue.offer(ny); 

                    //System.out.println(nx + ", " + ny);                   
                }
            }

        }

        return cnt;
    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        mat = new boolean[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int input = sc.nextInt();
                if (input == 0){
                    mat[i][j] = true;
                } 
            }
        }

        for(int k = 0; k < K; k++){
            int x = sc.nextInt()-1;
            int y = sc.nextInt()-1;

            pointX.add(x);
            pointY.add(y);
        }
        
        int ans = 0;

        for(int p = 0; p <  K; p++){
            int cx = pointX.get(p);
            int cy = pointY.get(p);

            if (canGo(cx, cy)){
                int result = bfs(cx, cy);
                ans += result;
            }
        }

        System.out.println(ans);

    }
}