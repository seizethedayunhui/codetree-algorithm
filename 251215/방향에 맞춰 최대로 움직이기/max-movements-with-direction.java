import java.util.*;

public class Main {

    public static int N;
    public static int[][] numsMat;
    public static int[][] directionsMat;

    public static int[] dx = { -1, -1, 0, 1, 1, 1, 0, -1 };
    public static int[] dy = { 0, 1, 1, 1, 0, -1, -1, -1 };

    public static ArrayList<Integer> arr = new ArrayList<>();

    public static int moves(int x, int y, ArrayList arr){

        if(!inRange(x, y, N)){
            return arr.size();
        }

        if (arr.size() > 0 && (int) arr.get(arr.size()-1) >= numsMat[x][y]) {
            System.out.println("탐색종료");
            for(int i = 0; i < arr.size(); i++){
                System.out.print(arr.get(i) + " ");
            }
            System.out.println();
            //System.out.println("(x, y) " + x + ", " + y + " 현재: " + numsMat[x][y] + ", 이전: " + (int) arr.get(arr.size()-1));
            //System.out.println();
            return arr.size();
        }

        int maxCnt = 0;
        int direction = directionsMat[x][y];
        int nx, ny;
        int k = 1;

        arr.add(numsMat[x][y]);

        while (true) {
            //System.out.println("현재 좌표: " + x + ", " + y);
        
            nx = x + dx[direction] * k;
            ny = y + dy[direction] * k;
            
            maxCnt = Math.max(maxCnt, moves(nx, ny, arr));
            k++;
        }

        arr.remove(arr.size()-1);

        System.out.println("완전종료: ");

        for(int i = 0; i < arr.size(); i++){
            System.out.print(arr.get(i) + " ");
        }

        System.out.println();
        System.out.println();

        
        

        return maxCnt;
    }

    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    public static void main(String[] args) {

       Scanner sc = new Scanner(System.in);

       N = sc.nextInt();
       numsMat = new int[N][N];
       directionsMat = new int[N][N];

       for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            numsMat[i][j] = sc.nextInt();
        }
       }

       for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            directionsMat[i][j] = sc.nextInt() -1;
        }
       }
    
        int r = sc.nextInt() - 1;
        int c = sc.nextInt() - 1;
        int ans = moves(r, c, arr);
        System.out.println(ans);

    }
}