import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt(); // 도착지점


        int minSeconds = Integer.MAX_VALUE;

        // i가 속도를 꺾는 위치임.
        // 딱 한번 꺾음. 그리고, 속도가 1이 되면 더 이상 줄이지 않고 유지함. 
        for (int i = 1; i < X; i++ ){

            int currentLocation = 0;
            int velocity = 1;
            int seconds = 0;
            boolean flag = false;

            while (currentLocation <= X) {

                currentLocation += (velocity);
                seconds += 1;
                // System.out.println(seconds + ", " + currentLocation + ", " + velocity);

                // 위치에 도달한 경우 break
                if (currentLocation == X){
                    if (velocity == 1){
                        flag = true;
                    }
                    break;

                } else if (currentLocation >= i) {

                    // 남은 거리
                    int remainingDistance = X - currentLocation;
                
                    // 이 다음에까지 현재 속도를 유지했을 때도 가능한 경우
                    int predictDistance = (velocity * (velocity + 1)) / 2;

                    if (remainingDistance < predictDistance){
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