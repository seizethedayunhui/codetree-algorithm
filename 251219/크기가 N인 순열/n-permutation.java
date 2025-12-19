import java.util.*;

public class Main {

    public static int N;
    public static ArrayList<Integer> arr = new ArrayList<>();

    public static boolean[] visited;

    public static void printPer(){
        for(int i = 0; i < arr.size(); i++ ){
            System.out.print(arr.get(i) + " ");
        }
        System.out.println();
        return;
    }

    public static void makePer(){

        if (arr.size() == 3){
            printPer();
            return;
        }

        for(int i = 1; i < N+1; i++){

            if (visited[i]){
                continue;
            }

            arr.add(i);
            visited[i] = true;
            makePer();

            arr.remove(arr.size()-1);
            visited[i] = false;
        }

        return;
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        visited = new boolean[N+1];

        makePer();
    }
}