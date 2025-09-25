import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String command;
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i = 0; i < N; i++){
            command = sc.next();
            if (command.equals("push_front")){
                dq.addFirst(sc.nextInt()); 
            } else if (command.equals("push_back")){
                dq.addLast(sc.nextInt());
            } else if (command.equals("pop_front")){
                System.out.println(dq.pollFirst());
            } else if (command.equals("pop_back")){
                System.out.println(dq.pollLast());
            } else if (command.equals("size")){
                System.out.println(dq.size());
            } else if (command.equals("empty")){
                int ans = (dq.isEmpty()) ? 1 : 0;
                System.out.println(ans);
            } else if (command.equals("front")){
                System.out.println(dq.peekFirst());
            } else {
                System.out.println(dq.peekLast());
            }
        }
    }
}