import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

       int[][] mat = new int[4][4];
       int[][] temp = new int[4][4];

       for (int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            int element = sc.nextInt();
            mat[i][j] = element;
            temp[i][j] = element;
        }
       }

       String direc = sc.next();

        int idx;
        if (direc.equals("L")){
            idx = 0;
        } else if (direc.equals("R")){
            idx = 1;
        } else if (direc.equals("U")){
            idx = 2;
        } else {
            idx = 3;
        }

        int startIdx, endIdx, d;
        if (idx % 2 != 0){
            startIdx = 3;
            endIdx = 0;
            d = -1;
        } else {
            startIdx = 0;
            endIdx = 3;
            d = 1;
        }

        if ( idx < 2 ){
            // 행 기준
            for(int row = 0; row < 4; row++){
                for(int i = startIdx; i != endIdx; ){
                    if(temp[row][i]==0){
                        temp[row][i] = temp[row][i+d];
                        temp[row][i+d] = 0;
                    }
                    i += d;
                }
            }
            for(int row = 0; row < 4; row++){
                for(int i = startIdx; i != endIdx; ){

                    if(temp[row][i] == temp[row][i+d]){
                        temp[row][i] += temp[row][i+d];
                        temp[row][i+d] = 0;
                    }
                    i += d;
                }
            }
            for(int row = 0; row < 4; row++){
                for(int i = startIdx; i != endIdx; ){
                    if(temp[row][i]==0){
                        temp[row][i] = temp[row][i+d];
                        temp[row][i+d] = 0;
                    }
                    i += d;
                }
            }
            
        } else {

            // 열기준
            for(int col = 0; col < 4; col++){
                for(int j = startIdx; j != endIdx; ){
                    if(temp[j][col]==0){
                        temp[j][col] = temp[j+d][col];
                        temp[j+d][col] = 0;
                    }

                    j += d;
                }
            }

            for(int col = 0; col < 4; col++){
                for(int j = startIdx; j != endIdx; ){

                    if (temp[j][col] == temp[j+d][col]){
                        temp[j][col] += temp[j+d][col];
                        temp[j+d][col] = 0;
                    }
                    j += d;
                }
            }
            
            for(int col = 0; col < 4; col++){
                for(int j = startIdx; j != endIdx; ){
                    if(temp[j][col]==0){
                        temp[j][col] = temp[j+d][col];
                        temp[j+d][col] = 0;
                    }

                    j += d;
                }
            }

        }

        for (int x = 0; x < 4; x++){
            for(int y = 0; y < 4; y++){
                mat[x][y] = temp[x][y];
                System.out.print(mat[x][y] + " ");
            }
            System.out.println();
        }
        
    }
}