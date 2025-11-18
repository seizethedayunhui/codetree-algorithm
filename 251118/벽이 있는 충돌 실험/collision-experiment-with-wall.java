import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    // 격자 범위 확인 함수
    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    // 메인 로직
    public static void main(String[] args) throws IOException { // I/O 예외 처리 필수
        // 🚨 Scanner 대신 BufferedReader와 StringTokenizer 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        // 테스트 케이스 루프
        for (int t = 0; t < T; t++){
            
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // ... (배열 선언 생략)
            int[] directions = new int[M];
            int[][] points = new int[M][2];
            boolean[] flags = new boolean[M];

            // 방향 벡터 (0:R, 1:D, 2:L, 3:U)
            int[] dx = { 0, 1, 0, -1};
            int[] dy = { 1, 0, -1, 0};

            // 초기 입력 및 상태 설정
            for(int m = 0; m < M; m++){
                st = new StringTokenizer(br.readLine()); // 매 줄마다 새로운 StringTokenizer
                
                int i = Integer.parseInt(st.nextToken());
                int j = Integer.parseInt(st.nextToken());
                String direc = st.nextToken();

                i--; j--; // 0-based 인덱스로 변환

                points[m][0] = i;
                points[m][1] = j;
                flags[m] = true;

                int direction;
                if (direc.equals("R")){
                    direction = 0;
                } else if (direc.equals("D")){
                    direction = 1;
                } else if (direc.equals("L")){
                    direction = 2;
                } else {
                    direction = 3;
                }
                directions[m] = direction;
            }

            int time = 0;
            // 시간 루프
            while (time < 2 * N){ 
                
                // 1단계: 모든 구슬의 다음 위치 계산 및 충돌 카운트 (O(M) + O(N^2))
                int[][] nextMat = new int[N][N]; 
                
                for(int m = 0; m < M; m++){
                    if (!flags[m]) continue;

                    int x = points[m][0];
                    int y = points[m][1];
                    int currentDirec = directions[m];

                    int nx = x + dx[currentDirec];
                    int ny = y + dy[currentDirec];

                    if (inRange(nx, ny, N)){
                        // 다음 위치로 이동
                        points[m][0] = nx;
                        points[m][1] = ny;
                        nextMat[nx][ny] += 1;

                    } else {
                        // 벽에 부딪힘: 방향만 반대로 바꾸고 현재 위치 유지
                        currentDirec = (currentDirec + 2) % 4;
                        directions[m] = currentDirec;
                        nextMat[x][y] += 1;
                    } 
                }
                
                // 2단계: 충돌 확인 및 최종 상태 업데이트 (O(M))
                
                // 🚨 불필요한 collisionPoints 생성 코드 제거
                /*
                for(int k = 0; k < N; k++){
                    for(int l = 0; l < N; l++){
                        if (nextMat[k][l] >= 2){
                            collisionPoints.add(new int[]{k, l});
                        }
                    }
                }
                */

                // 충돌 구슬 비활성화 (O(M))
                for(int m = 0; m < M; m++){
                    if (flags[m]){
                        int x = points[m][0];
                        int y = points[m][1];
                        
                        // nextMat 배열의 값만 확인하여 비활성화
                        if (nextMat[x][y] >= 2) {
                            flags[m] = false;
                        }
                    }
                }
                
                time++;
            }

            // 최종 남은 구슬 개수 계산 (O(M))
            int cnt = 0;
            for(int m = 0; m < M; m++){
                if (flags[m]){
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}