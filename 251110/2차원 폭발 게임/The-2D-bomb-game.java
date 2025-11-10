import java.util.Scanner;

public class Main {
    
    // 폭탄 연쇄 폭발 및 중력 이동을 처리하는 재사용 가능한 메서드
    // isFinal: K번째 주기의 '회전 후' 처리인지 여부. (여기서는 모든 단계에서 동일 로직 적용)
    public static void processExplosionAndGravity(int N, int M, int[][] mat, int[][] temp) {

        
        // temp 배열을 mat 배열로 초기화 (작업은 temp에서 진행)
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                temp[i][j] = mat[i][j];
            }
        }

        boolean exploded = true;
        while(exploded) { // 폭탄이 터진다면 계속 반복
            exploded = false;
            
            // 1. 폭탄 처리 로직 (열(col) 단위 검사)
            for(int col = 0; col < N; col++){
                int startIdx = 0;
                int currentCnt = 0;
                // temp[0][col]이 0일 수 있으므로, 0이 아닌 첫 요소를 찾아 초기화해야 더 정확하지만,
                // 현재 로직은 0을 하나의 '요소'로 간주하고 연속성을 끊는 방식으로 작동하므로 유지
                int currentElement = temp[0][col]; 
                
                // 폭발할 영역을 찾아 temp 배열에 0으로 표시
                for(int row = 0; row < N; row++){
                    
                    if (temp[row][col] == currentElement){
                        currentCnt += 1;
                    } else {
                        // 연속된 요소가 끝났을 때 폭발 여부 검사
                        if (currentCnt >= M && currentElement != 0){
                            for (int l = startIdx; l < row; l++){
                                if(temp[l][col] != 0) {
                                    temp[l][col] = 0;
                                    exploded = true;
                                }
                            }
                        }

                        // 새로운 연속 요소 시작
                        startIdx = row;
                        currentCnt = 1;
                        currentElement = temp[row][col];
                    }
                }
                
                // 열의 마지막 부분 폭발 처리
                if (currentCnt >= M && currentElement != 0){
                    for (int m = startIdx; m < N; m++){
                        if(temp[m][col] != 0) {
                            temp[m][col] = 0;
                            exploded = true;
                        }
                    }
                }
            }

            if (!exploded) break; // 폭발이 없었다면 중력 이동 없이 연쇄 폭발 루프 종료
            
            // 2. 중력 처리 로직 (temp에서 0을 위로 올림)
            for(int c = 0; c < N; c++){
                for(int r = N-1; r > -1; r--){
                    if(temp[r][c] == 0){
                        for(int nextRow = r-1; nextRow > -1; nextRow--){
                            if (temp[nextRow][c]!=0){
                                temp[r][c] = temp[nextRow][c];
                                temp[nextRow][c] = 0;
                                break;
                            }
                        }
                    }
                }
            }
        }
        
        // 최종 결과를 mat에 복사
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = temp[i][j];
            }
        }
        

    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 격자 크기
        int M = sc.nextInt(); // 폭발 최소 길이
        int K = sc.nextInt(); // 회전/폭발 주기 횟수

        int[][] mat = new int[N][N];
        int[][] temp = new int[N][N];

        // 초기 격자 입력
        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                mat[i][j] = sc.nextInt();
            }
        }
        sc.close();
        
        // K번의 주기 반복
        for(int k = 0; k < K; k++){
            
            // 1. 초기 폭발 및 연쇄 폭발 처리 (mat -> temp -> mat)
            processExplosionAndGravity(N, M, mat, temp);
            
            // 2. 시계 방향 회전 로직 (mat -> temp)
            for(int x = 0; x < N; x++){
                for(int y = 0; y < N; y++){
                    int nx = y;
                    int ny = N - x - 1;
                    temp[nx][ny] = mat[x][y];
                }
            }
            
            // 3. 회전 후 중력 처리 (temp에 중력 적용 후 -> mat)
            // 중력만 처리하므로, processExplosionAndGravity와 달리 중력 로직만 수행
            for(int c = 0; c < N; c++){
                for(int r = N-1; r > -1; r--){
                    if(temp[r][c] == 0){
                        for(int nextRow = r-1; nextRow > -1; nextRow--){
                            if (temp[nextRow][c]!=0){
                                temp[r][c] = temp[nextRow][c];
                                temp[nextRow][c] = 0;
                                break;
                            }
                        }
                    }
                }
            }
            
            // 회전/중력 결과를 mat에 복사
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    mat[i][j] = temp[i][j];
                }
            }
            
            // 4. 마지막 회전 후에도 연쇄 폭발 처리 (mat -> temp -> mat)
            // K번째 주기(회전)의 마지막에 발생한 폭발을 처리
            processExplosionAndGravity(N, M, mat, temp);
            
        } // K번 주기 종료

        // 최종 남은 요소 개수 계산
        int cnt = 0;
        for (int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(mat[i][j] != 0){
                    cnt += 1;
                }
            }
        }
        System.out.println(cnt);
    }
}