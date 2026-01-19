import java.util.*;

public class Main {

    public static int N, K, D, U;
    public static int[][] mat;
    public static ArrayList<int[]> countries = new ArrayList<>();
    public static int maxCnt = Integer.MIN_VALUE;

    public static ArrayList<int[]> selectedCountries = new ArrayList<>();
    public static int cnt_countries(int idx){

        if (selectedCountries.size() == K){
            return bfs();
        }

        if (idx == N*N){
            return maxCnt;
        }

        for (int i = idx; i < N*N; i++){
            int[] country = countries.get(i);
            selectedCountries.add(country);
            maxCnt = Math.max(cnt_countries(idx+1), maxCnt);
            selectedCountries.remove(selectedCountries.size()-1);
        }

        return maxCnt;
    }

    public static boolean inRange(int x, int y){
        return (( x >= 0 && x < N ) && ( y >= 0 && y < N ));
    }

    public static boolean canGo(int x, int y, boolean[][] visited){
        return ((inRange(x, y)) && (!visited[x][y]));
    }

    public static boolean heightDiff(int x, int y, int nx, int ny){
        int cPos = mat[x][y];
        int nPos = mat[nx][ny];

        int diff = Math.abs(cPos - nPos);

        return ( diff >= U && diff <= D );
    }

    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };

    public static int bfs(){

        int cnt = 0;
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][N];

        for (int i = 0; i < K; i++){
            int[] c = selectedCountries.get(i);
            q.offer(c);
            cnt += 1;
            visited[c[0]][c[1]] = true;
            //System.out.println(c[0] + ", " + c[1] + " 시작");
        }

        while (!q.isEmpty()){
            int[] currentC = q.poll();

            int x = currentC[0];
            int y = currentC[1];
            

            int nx, ny;
            for(int d = 0; d < 4; d++){
                nx = x + dx[d];
                ny = y + dy[d];

                if (canGo(nx, ny, visited) && heightDiff(x, y, nx, ny)){
                    //System.out.println(nx + ", " + ny);
                    int[] nextC = { nx, ny };
                    q.offer(nextC);
                    cnt++;
                    visited[nx][ny] = true;
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        U = sc.nextInt();
        D = sc.nextInt();

        mat = new int[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j]= sc.nextInt();
                int[] p = {i, j};
                countries.add(p);
            }
        }

        int ans = cnt_countries(0);
        System.out.println(ans);
    }
}