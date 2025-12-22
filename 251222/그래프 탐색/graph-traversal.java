import java.util.*;

public class Main {
    public static int N;
    public static int M;
    public static boolean[][] vertex;
    public static boolean[] visited;

    public static ArrayList<Integer> points = new ArrayList<>();

    public static int dfs(int idx, int find){

        for(int i = 0; i < N; i++){
            if (i == find){
                continue;
            }
            if ((!visited[i]) && (vertex[idx][i] && vertex[i][idx])){

                visited[i] = true;
                points.add(i);
                // System.out.println("들어옴 " + i + ", " + idx);
                dfs(i, find);
            }
        }

        return points.size();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        vertex = new boolean[N][N];
        visited = new boolean[N];

        for(int i = 0; i < M; i++){
            int e1 = sc.nextInt() - 1;
            int e2 = sc.nextInt() - 1;

            vertex[e1][e2] = true;
            vertex[e2][e1] = true;
        }

        int ans = dfs(0, 0);
        System.out.println(ans);
    }
}