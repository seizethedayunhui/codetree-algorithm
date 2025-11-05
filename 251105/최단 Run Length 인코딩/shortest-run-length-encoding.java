import java.util.*;

public class Main {

    public static int getLength(String str, int N){
            boolean flag = false;
            int cnt = 0;
            String element = ""
;           String newString = "";
            String currentLength;
            String newSubString;

            for(int i = 0; i < N; i++){
                if ( flag && element.equals(String.valueOf(str.charAt(i)))){
                    cnt += 1;
                    
                } else {
                    
                    currentLength = Integer.toString(cnt);
                    newSubString = (element + currentLength);
                    newString += newSubString;

                    cnt = 1;
                    element = String.valueOf(str.charAt(i));
                    flag = true;
                }

                if (i == N-1){

                    currentLength = Integer.toString(cnt);
                    newSubString = element + currentLength;
                    newString += newSubString;

                }
            }
            // System.out.println(str + ", " + newString);
            return newString.substring(1).length();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String A = sc.next();
        int N = A.length();

        int minLength = Integer.MAX_VALUE;


        for(int i = 0; i < N-1; i++){

            char temp = A.charAt(N-1);
            A = String.valueOf(temp) + A.substring(0, N-1); // shift 한 문자열

            minLength = Math.min(minLength, getLength(A, N));
        }

        System.out.println(minLength);
    }
}