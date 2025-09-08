import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];

        int idx = 0;

        for(int i = 0; i <N; i++){

            String cmd;
            int num;

            cmd = sc.next();

            if (cmd.equals("push_back")== true) {
                num = sc.nextInt();
                arr[idx] = num;
                idx++;
            } else if (cmd.equals("pop_back") == true) {
                idx--;
                arr[idx] = 0;
            } else if (cmd.equals("size") == true) {
                System.out.println(idx);
            }else {
                num = sc.nextInt();
                System.out.println(arr[num-1]);
            }

        }
    }
}