import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String currentWinner = "None";

        int scoreA = 0;
        int scoreB = 0;

        int cnt = 0;

        for(int i = 0; i < N; i++){
            String who = sc.next();
            int change = sc.nextInt();

            if (who.equals("A")){
                scoreA += change;
            } else {
                scoreB += change;
            }

            if (currentWinner.equals("None")){

                if (scoreA > scoreB){
                    currentWinner = "A";
                    cnt += 1;
                } else if (scoreA < scoreB) {
                    currentWinner = "B";
                    cnt += 1;
                } 

            } else if ( currentWinner.equals("Both")){

                if (scoreA > scoreB){
                    currentWinner = "A";
                    cnt += 1;
                } else if (scoreA < scoreB) {
                    currentWinner = "B";
                    cnt += 1;
                } 

            } else if ( currentWinner.equals("A")){

                if (scoreA == scoreB) {
                    currentWinner = "Both";
                    cnt += 1;
                } else if (scoreA < scoreB) {
                    currentWinner = "B";
                    cnt += 1;
                }
                
            } else if ( currentWinner.equals("B")){

                if (scoreA > scoreB){
                    currentWinner = "A";
                    cnt += 1;
                } else if (scoreA == scoreB) {
                    currentWinner = "Both";
                    cnt += 1;
                } 

            }
        }

        System.out.println(cnt);
    }
}