import java.util.*;

public class Main {
    public static void main(String[] args) {

        LinkedList<Integer> l = new LinkedList<>();

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for(int i = 0; i < N; i++){

            String cmd = sc.next();
            int num = 0;
            int idx = 0;

            if (cmd.equals("push_front")){

                num = sc.nextInt();
                l.addFirst(num);

            } else if (cmd.equals("push_back")){

                num = sc.nextInt();
                l.addLast(num);

            } else if (cmd.equals("pop_front")){

                System.out.println(l.pollFirst());

            } else if (cmd.equals("pop_back")){

                System.out.println(l.pollLast());
                 
            } else if (cmd.equals("size")){

                System.out.println(l.size());


            } else if (cmd.equals("empty")){

                if(!l.isEmpty()){

                    // 비어있으면 0을 출력
                    System.out.println(0);
                } else {
                    System.out.println(1);
                }

                

            } else if (cmd.equals("front")){

                System.out.println(l.peekFirst());

            } else {

                System.out.println(l.peekLast());

            }
        }
    }
}