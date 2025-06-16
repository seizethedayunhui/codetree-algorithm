import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x1, y1, x2, y2 ;

        x1 = sc.nextInt();
        y1 = sc.nextInt();
        x2 = sc.nextInt();
        y2 = sc.nextInt();

        int a1, b1, a2, b2;

        a1 = sc.nextInt();
        b1 = sc.nextInt();
        a2 = sc.nextInt();
        b2 = sc.nextInt();

        boolean flag = false;

        if ((x2 < a1) || (a2 < x1)){
            flag = true;
        }

        if (flag){
            System.out.println("nonoverlapping");
        } else {
            System.out.println("overlapping");
        }
        
    }
}