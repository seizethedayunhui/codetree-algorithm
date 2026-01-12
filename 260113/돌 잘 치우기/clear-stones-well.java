import java.util.*;

public class Main {
    public static int N;
    public static int K;
    public static int M;

    public static boolean[][] mat;

    public static boolean[][] visited;
    public static Queue<int[]> q = new ArrayDeque<>();
    public static ArrayList<int[]> points = new ArrayList<>();
    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };

    public static boolean inRange(int x, int y){
        return (( x >= 0 && x < N ) && ( y >= 0 && y < N ) );
    }

    // 방문가능한지 여부
    public static boolean canGo(int x, int y){
        return (inRange(x, y) && mat[x][y] && !visited[x][y] );
    }

    public static int bfs(){

        // for(int i = 0; i < N; i++){
        //     for(int j = 0; j < N; j++){
        //         System.out.print(mat[i][j]+ " ");
        //     }
        //     System.out.println();
        // }
        // System.out.println();

        int cnt = 0;
        visited = new boolean[N][N];

        for(int k = 0; k < K; k++){

            int[] point = points.get(k);

            if (canGo(point[0], point[1])){

                visited[point[0]][point[1]] = true;
                q.offer(point);
                cnt++;

                while(!q.isEmpty()){

                    int[] e = q.poll();
                    int cx = e[0];
                    int cy = e[1];

                    int nx, ny;

                    for(int i = 0; i < 4; i++){
                        nx = cx + dx[i];
                        ny = cy + dy[i];

                        if (canGo(nx, ny)){
                            cnt++;
                            visited[nx][ny] = true;
                            int[] ne = {nx, ny};
                            q.offer(ne);
                        }
                    }

                }
            }
        }

        return cnt;
    }

    public static ArrayList<int[]> rocks = new ArrayList<>();
    public static ArrayList<int[]> selectedRocks = new ArrayList<>();

    public static int maxCnt = Integer.MIN_VALUE;

    public static int backTracking(int idx){

        if (selectedRocks.size() == M){
            // System.out.println(selectedRocks.size());
            // for(int i = 0; i < M; i++){
            //     System.out.println(selectedRocks.get(i)+ " ");
            // }
            // System.out.println();
            // 상하좌우로 인접한 곳 이동 개수 cnt 함수
            return bfs();
        }

        if (idx == rocks.size()){
            return maxCnt;
        }

        for(int i = idx; i < rocks.size(); i++){

            int[] element = rocks.get(i);
            int x, y;
            
            // 선택하는 경우
            selectedRocks.add(element);
            x = element[0];
            y = element[1];
            mat[x][y] = true;
            maxCnt = Math.max(maxCnt, backTracking(idx+1));

            // 선택하지 않는 경우(원래대로 복귀)
            selectedRocks.remove(selectedRocks.size()-1);
            mat[x][y] = false;
        }

        return maxCnt;
        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        M = sc.nextInt();

        mat = new boolean[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int e = sc.nextInt();
                if (e == 1){
                    int[] p = {i, j};
                    rocks.add(p);
                    mat[i][j] = false;
                } else {
                    mat[i][j] = true;
                }
                
            }
        }

        for(int k = 0; k < K; k++){
            int r = sc.nextInt()-1;
            int c = sc.nextInt()-1;
            int[] point = {r, c};
            points.add(point);
        }

        int ans = backTracking(0);
        System.out.println(ans);
    }
}