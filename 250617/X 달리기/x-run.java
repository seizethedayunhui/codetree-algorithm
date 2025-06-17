import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt(); // 도착지점


        int minSeconds = Integer.MAX_VALUE;

        // i가 속도를 꺾는 위치임.
        // 딱 한번 꺾음. 그리고, 속도가 1이 되면 더 이상 줄이지 않고 유지함. 
        for (int i = 1; i < X + 1; i++ ){

            int currentLocation = 0;
            int velocity = 1;
            int seconds = 0;
            boolean flag = false;

            while (true) {

                currentLocation += (velocity);
                seconds += 1;
                // System.out.println(seconds + ", " + currentLocation + ", " + velocity);

                // 위치에 도달한 경우 break
                if (currentLocation == X){
                    if (velocity == 1){
                        flag = true;
                    }
                    break;
                } else if (currentLocation >= i){
                    // 속도가 1인 경우 유지해야함. 
                    if (velocity != 1){
                        velocity -= 1;
                    }
                } else {
                    velocity += 1;
                }
                
    
            }
            
            if (flag){
                minSeconds = Math.min(minSeconds, seconds);
            }
            
        }

         System.out.println(minSeconds);


    }
}