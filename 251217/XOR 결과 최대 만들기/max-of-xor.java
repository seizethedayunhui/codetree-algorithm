import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arr;
    public static ArrayList<Integer> seq = new ArrayList<>();

    public static int XOR(){
        int x = seq.get(0);

        for(int j = 1; j < M; j++){
            x = x ^ seq.get(j);
        }

        return x;
    }

    public static int maxXOR(int idx){

        if (seq.size() == M){
            // XOR 연산
            int value = XOR();
            // for(int j = 0; j < M; j++){
            //     System.out.print(seq.get(j) + " ");
            // }
            // System.out.println();
            // System.out.println(value);
            return value;
        }

        int maxCnt = 0;
        for(int i = idx; i < N; i++){
            seq.add(arr[i]);
            maxCnt = Math.max(maxCnt, maxXOR(i+1));
            seq.remove(seq.size()-1);
        }

        return maxCnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
        }

        int ans = maxXOR(0);
        System.out.println(ans);
    }
}