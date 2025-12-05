import java.util.*;

public class Main {
    public static int N;
    public static int[] record = new int[1000];
    public static int[][] points;

    public static int ans;

    public static boolean addRecord(int l, int r){

        boolean flag = true;    
        System.out.println("들어옴2");

        for(int j = l; j <= r; j++){
            if (record[j] != 0){
                flag = false;
                break;
            } else {
                record[j] += 1;
            }
        }
        return flag;
    }
    
    public static void removeRecord(int l, int r){
        for(int j = l; j <= r; j++){
            record[j] -= 1;
        }        
    }

    public static void cntLines(int idx, int N, int cnt){
        System.out.println("들어옴");
        
        if (idx >= N){
            // return 현재까지의 선분 cnt값
            ans = Math.max(ans, cnt);
            
            return;
        }
        
        int left = points[idx][0];
        int right = points[idx][1];

        // 넣는지 파악
        if (addRecord(left, right)){
            cntLines(idx++, N, cnt++);
            removeRecord(left, right);
            
        }

        // 안 넣는다
        cntLines(idx++, N, cnt);

    }

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       N = sc.nextInt();
       
       points = new int[N][2];
       for(int i = 0; i < N; i++){
            int l = sc.nextInt();
            int r = sc.nextInt();
            points[i][0] = l;
            points[i][1] = r;
       }

        cntLines(0, N, 0);

        System.out.println(ans);
    }
}