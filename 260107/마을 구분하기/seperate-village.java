import java.util.*;

public class Main {

    public static ArrayList<Integer> people = new ArrayList<>();
    public static int peopleCnt;
    public static int N;
    public static boolean[][] mat;
    public static boolean[][] visited;
    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };

    public static boolean inRange(int x, int y){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    public static boolean canGo(int x, int y){
        return inRange(x, y) && mat[x][y] && !visited[x][y];
    }

    public static void dfs(int x, int y){
        visited[x][y] = true;
        peopleCnt++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (canGo(nx, ny)) {
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        mat = new boolean[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                mat[i][j] = sc.nextInt() == 1;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (canGo(i, j)) {
                    peopleCnt = 0;   // 새 영역 시작 시 카운트 초기화
                    dfs(i, j);       // DFS로 영역 탐색
                    people.add(peopleCnt); // 영역 크기 저장
                }
            }
        }

        Collections.sort(people);
        System.out.println(people.size());
        for (int cnt : people) {
            System.out.println(cnt);
        }
    }
}
