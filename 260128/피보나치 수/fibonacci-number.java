import java.util.*;

public class Main {

    public static int[] f;

    public static int fibo(int n){

        if (f[n] != -1){
            return f[n];
        } else if (n <= 2){
            f[n] = 1;
        } else {
            f[n] = fibo(n-1) + fibo(n-2);
        }

        return f[n];

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        f = new int[N+1];
        for(int i = 0; i < N+1; i++){
            f[i] = -1;
        }

        int ans = fibo(N);
        System.out.println(ans);
    }
}