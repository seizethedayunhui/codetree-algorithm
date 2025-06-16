import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b;
        
        a = sc.nextInt();
        b = sc.nextInt();

        int c, d;

        c = sc.nextInt();
        d = sc.nextInt();


        int[] records = new int[101];
        for( int i = a; i < b; i++){
            records[i] += 1;
        }

        for ( int j = c; j < d; j++){
            records[j] += 1;
        }

        int cnt = 0;
        for (int rc : records){
            if (rc >= 1){
                cnt += 1;
            }
        }

        System.out.println(cnt);
        
    }
}