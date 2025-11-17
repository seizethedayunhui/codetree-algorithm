import java.util.*;

public class Main {

    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        int[][] apples = new int[N][N];
        int[][] snake = new int[N][N];

        for(int i = 0; i < M; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            x--;
            y--;
            apples[x][y] = 1;
        }
        
        String[] directions = new String[K];
        int[] moves = new int[K];

        for(int i = 0; i < K; i++){
            directions[i] = sc.next();
            moves[i] = sc.nextInt();
        }

        int[] dx = { 0, 1, 0, -1};
        int[] dy = { 1, 0, -1, 0};

        int headX = 0;
        int headY = 0;
        int tailX = 0;
        int tailY = 0;

        snake[headX][headY] = 1;

        int direction = -1;
        int time = 0;
        boolean flag = true;

        int idx = 0;
        ArrayList<int[]> prevPoints = new ArrayList<>();

        for(int i = 0; i < K; i++){

            String currentDirec = directions[i];
            int move = moves[i];

            // 방향 전환
            if (currentDirec.equals("R")) direction = 0;
            else if (currentDirec.equals("D")) direction = 1;
            else if (currentDirec.equals("L")) direction = 2;
            else direction = 3;

            for(int j = 0; j < move; j++){

                int nx = headX + dx[direction];
                int ny = headY + dy[direction];
                time++;

                // 맵 밖
                if (!inRange(nx, ny, N)) {
                    flag = false;
                    break;
                }
                                    // head 이동
                headX = nx;
                headY = ny;
                
                prevPoints.add(new int[]{headX, headY});

                // 사과가 없는 경우 tail 이동
                if (apples[nx][ny] == 0) {
                    int[] nextTail = prevPoints.get(idx);
                    int px = nextTail[0];
                    int py = nextTail[1];

                    snake[tailX][tailY] = 0; // 꼬리 제거
                    tailX = px;
                    tailY = py;
                    idx++;
                } else {
                    // 사과 먹은 자리 0으로
                    apples[nx][ny] = 0;
                }

                // 자기 몸과 충돌
                if (snake[nx][ny] == 1) {
                    flag = false;
                    break;
                }
                snake[headX][headY] = 1;
            }

            if (!flag) break;
        }

        System.out.println(time);
    }
}
