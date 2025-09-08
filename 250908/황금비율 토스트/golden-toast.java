import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        String code = sc.next();

        LinkedList<Character> l = new LinkedList<>();

        for(int i = 0; i < N; i++){
            l.addLast(code.charAt(i));
        }

        ListIterator<Character> it = l.listIterator(l.size());

        for (int i = 0; i < M; i++){

            String cmd = sc.next();

            if (cmd.equals("L")){

                if(it.hasPrevious()){
                    it.previous();
                }

            } else if (cmd.equals("R")){

                if(it.hasNext()){
                    it.next();
                }

            } else if (cmd.equals("D")){

                if(it.hasNext()){
                    it.next();
                    it.remove();
                }               

            } else if (cmd.equals("P")){
            String cha = sc.next();
                it.add(cha.charAt(0));
            }
        }

        it = l.listIterator();
        while(it.hasNext()){
            System.out.print(it.next());
        }
        
    }
}