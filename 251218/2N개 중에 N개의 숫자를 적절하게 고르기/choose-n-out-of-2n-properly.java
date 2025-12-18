import java.util.*;

public class Main {
    public static int N;
    public static int entireSum = 0;
    public static ArrayList<Integer> arr = new ArrayList<>();
    public static ArrayList<Integer> select = new ArrayList<>();

    public static int calcDiff(){
        int A = 0;
        for(int i = 0; i < N; i++){
            int index = select.get(i);
            A += arr.get(index);
        }
        int B = Math.abs(entireSum - A);
        int diff = Math.abs(A - B);

        return diff;
    }

    public static int findMinDiff(int idx){

        if (select.size() == N){
            return calcDiff();
        }

        if (idx == 2*N){
            return  Integer.MAX_VALUE;
        }

        int minDiff = Integer.MAX_VALUE;

        for(int i = idx; i < 2*N; i++){
            select.add(i);
            minDiff = Math.min(minDiff, findMinDiff(i+1));
            select.remove(select.size()-1);
        }

        return minDiff;
    }

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for(int i = 0; i < 2*N; i++){
            int element = sc.nextInt();
            arr.add(element);
            entireSum += element;
        }

        int ans = findMinDiff(0);
        
        System.out.println(ans);
    }
}