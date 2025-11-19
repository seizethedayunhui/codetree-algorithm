import java.util.*;

public class Main {
    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int T = sc.nextInt();
        int K = sc.nextInt();

        ArrayList<ArrayList<Integer>>[][] mat = new ArrayList[50][50];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = new ArrayList<>();
            }
        }

        int[][] points = new int[M][2];
        int[] directions = new int[M];
        int[] velocity = new int[M];
        boolean[] flag = new boolean[M];

        for(int i = 0; i < M; i++){

            points[i][0] = sc.nextInt() - 1;
            points[i][1] = sc.nextInt() - 1;

            String direction = sc.next();
            if(direction.equals("R")){
                directions[i] = 0;
            } else if (direction.equals("D")){
                directions[i] = 1;
            } else if (direction.equals("L")){
                directions[i] = 2;
            } else {
                directions[i] = 3;
            }

            velocity[i] = sc.nextInt();
            flag[i] = true;
        }

        int[] dx = { 0, 1, 0, -1};
        int[] dy = { 1, 0, -1, 0};

        int x, y, nx, ny, v, d;

        for(int t = 0; t < T; t++){

            for(int m = 0; m < M; m++){

                if (!flag[m]) continue;

                x = points[m][0];
                y = points[m][1];
                d = directions[m];
                v = velocity[m];

                mat[x][y].remove((Object) m);

                for(int j = 0; j < v; j++){

                    nx = x + dx[d];
                    ny = y + dy[d]; 

                    if(!inRange(nx, ny, N)){
                        // 방향 change
                        d = (d+2) % 4;
                        nx = x + dx[d];
                        ny = y + dy[d];
                    }  

                    x = nx; 
                    y = ny;                
                }

                // 좌표랑 방향 갱신
                points[m][0] = x;
                points[m][1] = y;
                directions[m] = d;

                ArrayList<Integer> arr = new ArrayList<>();
                arr.add(v);
                arr.add(m);

                // 현재 위치 추가
                mat[x][y].add(arr);
                
            } 

            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){

                    // 길이 초과하는 경우 
                    if(mat[i][j].size() >= K){

                        // 정렬 진행
                        mat[i][j].sort(Comparator.<ArrayList<Integer>>comparingInt(o -> o.get(0))
                         .thenComparingInt(o -> o.get(1)));
                        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
                        // 비교
                        for(int k = 0; k < mat[i][j].size(); k++){

                            if(k >= K){
                                int idx = mat[i][j].get(k).get(1);
                                flag[idx] = false;
                            } else {
                                arr.add(mat[i][j].get(k));
                            }
                        }

                        mat[i][j] = arr;
                        

                    }
                }
            }
            
        }

        int cnt = 0;
        for (int m = 0; m < M; m++){
            if (flag[m]){
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}