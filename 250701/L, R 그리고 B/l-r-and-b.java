import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[][] mat = new String[10][10];

        for(int i = 0; i < 10; i++){

            String input = sc.next();
            for(int j = 0; j < 10; j++){
                 mat[i][j] = String.valueOf(input.charAt(j)); // char → String 변환
            }
        }

        int startX = 0;
        int startY = 0;
        int endX = 0;
        int endY = 0;

        boolean startFlag = false;

        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){

                if ( mat[i][j].equals("L") || mat[i][j].equals("B")){
                    if(!startFlag){
                        startX = i;
                        startY = j;
                        startFlag = true;
                    } else {
                        endX = i;
                        endY = j;
                    }
                }

            }
        }
   

        int cnt = 0;
        while (true) {

            int nextX, nextY;

            if (startX == endX){

                if (startY > endY){
                    nextX = startX;
                    nextY = startY - 1;                   
                } else {
                    nextX = startX;
                    nextY = startY + 1; 
                }

            } else if (startX > endX) {
                
                if (startY == endY){

                    nextX = startX - 1;
                    nextY = startY;
                } else {
                    nextX = startX;
                    nextY = startY + 1;
                }

            } else {

                nextX = startX + 1;
                nextY = startY;

            }


            if (mat[nextX][nextY].equals("R") ){

                if (startX == endX){
                    nextX = startX + 1;
                    nextY = startY;
                } else {
                    nextX = startX;
                    nextY = startY + 1;
                }

            }

            startX = nextX;
            startY = nextY;


            // 목적지에 도착한 경우를 처리해주기 위해서는 if - else문을 가장 마지막에 추가해주어야 함.
            if (startX == endX && startY == endY){
                break;
            } else {
                cnt += 1;
            }
        }

        System.out.println(cnt);
        
    }
}