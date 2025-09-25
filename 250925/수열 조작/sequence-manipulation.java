import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        Deque<Integer> dq = new ArrayDeque<>();

        for(int i = 0; i < N; i++){
            dq.addLast(i+1);
        }

        while(dq.size()!=1){
            // 맨 앞의 정수 제거
            dq.pollFirst();
            // 남은 수열의 맨 앞 정수를 맨 뒤로 이동 시킴
            int element = dq.pollFirst();
            dq.addLast(element);
        }

        System.out.println(dq.pollFirst());
    }
}