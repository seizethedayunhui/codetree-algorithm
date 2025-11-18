import java.util.*;

public class Main {

    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++){
            int N = sc.nextInt();
            int M = sc.nextInt();

            int[][] mat = new int[N][N];
            int[] directions = new int[M];
            int[][] points = new int[M][2];
            boolean[] flags = new boolean[M];

            int[] dx = { 0, 1, 0, -1};
            int[] dy = { 1, 0, -1, 0};

            for(int m = 0; m < M; m++){

                int i = sc.nextInt();
                int j = sc.nextInt();

                i--;
                j--;

                mat[i][j] = 1;

                // 점의 위치 
                int[] point = { i, j };
                points[m] = point;

                String direc = sc.next();

                int direction;
                if (direc.equals("R")){
                    direction = 0;
                } else if (direc.equals("D")){
                    direction = 1;
                } else if (direc.equals("L")){
                    direction = 2;
                } else {
                    direction = 3;
                }
                directions[m] = direction;
                flags[m] = true;
            }

            int time = 0;
            int x, y, nx, ny;
            int currentDirec;

            while (time < 100){
                
                for(int m = 0; m < M; m++){

                    if (flags[m]){

                        x = points[m][0];
                        y = points[m][1];

                        currentDirec = directions[m];

                        nx = x + dx[currentDirec];
                        ny = y + dy[currentDirec];

                        if (inRange(nx, ny, N)){

                            mat[x][y] -= 1;

                            x = nx;
                            y = ny;

                            mat[x][y] += 1;

                            points[m][0] = x;
                            points[m][1] = y;

                        } else {
                            currentDirec = (currentDirec + 2) % 4;
                            directions[m] = currentDirec;
                        }  

                    }
                }

                for(int k = 0; k < N; k++){
                    for(int l = 0; l < N; l++){
                        if (mat[k][l] >= 2){
                            // System.out.println("2개 이상 겹쳐진 곳 " + k +", " + l);
                            for(int j = 0; j < M; j++){
                                if (points[j][0] == k && points[j][1] == l){
                                    flags[j] = false;
                                }
                            }

                            mat[k][l] = 0;
                        }
                    }
                }
                time++;
            }

            int cnt = 0;
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    cnt += mat[i][j];

                    //System.out.print(mat[i][j] + " ");
                }
                //System.out.println();
            }

            System.out.println(cnt);
        }
    }
}