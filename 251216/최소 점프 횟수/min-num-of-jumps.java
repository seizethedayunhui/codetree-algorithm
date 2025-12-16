import java.util.*;

public class Main {

    public static ArrayList<Integer> arr = new ArrayList<>();
    public static ArrayList<Integer> jumpStamp = new ArrayList<>();
    public static int N;
    public static final int MAX_JUMP = 100;

    // idx = 현재위치
    // 그렇다면..........................
    public static int jump(int idx){

        if (idx > 0 && jumpStamp.get(jumpStamp.size()-1) == N-1){
            // for(int i = 0; i < jumpStamp.size(); i++){
            //     System.out.print(jumpStamp.get(i) + " ");
            // }
            // System.out.println();
            // System.out.println();
            return jumpStamp.size();
        }

        int jumpRange = (int) arr.get(idx);
        int minJumpCnt = MAX_JUMP;

        for(int i = 1; i < jumpRange + 1; i++){
            int nx = idx + i;
            jumpStamp.add(nx);
            minJumpCnt = Math.min(minJumpCnt, jump(nx));
            // System.out.println(minJumpCnt);
            jumpStamp.remove(jumpStamp.size()-1);
        }

        return minJumpCnt;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for(int i = 0; i < N; i++){
            int e = sc.nextInt();
            arr.add(e);
        }
        
        int ans = jump(0);

        if (ans == MAX_JUMP){
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }

    }
}