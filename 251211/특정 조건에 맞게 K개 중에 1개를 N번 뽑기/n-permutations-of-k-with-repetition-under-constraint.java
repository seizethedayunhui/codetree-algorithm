import java.util.*;

public class Main {
    public static ArrayList<Integer> arr = new ArrayList<>();
    public static int N;
    public static int K;

    public static void printPair(ArrayList<Integer> a){
        for(int i = 0; i < a.size(); i++){
            System.out.print(a.get(i) + " ");
        }
        System.out.println();
    }

    public static boolean checkCond(ArrayList<Integer> a){
        
        int start = a.size()-1;
        boolean flag = false;
        for(int k = start - 1; k > start - 3; k--){
            if ( a.get(k) != a.get(start) ){
                flag = true;
                return flag;
            }
        }
        return flag;
    }

    public static void orderedPair(int N, int K, ArrayList<Integer> a){

        if (a.size() >= 3){
            if (!checkCond(a)){
                return;
            }
        }

        if (a.size() == N){
            printPair(a);
            return;
        }

        for(int j = 1; j < K + 1; j++){
            a.add(j);
            orderedPair(N, K, a);
            a.remove(a.size()-1);
        }
        return;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        K = sc.nextInt();
        N = sc.nextInt();

        orderedPair(N, K, arr);
    }
}