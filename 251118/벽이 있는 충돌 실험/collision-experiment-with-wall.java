import java.util.*;

public class Main {

    // 격자 범위 확인 함수
    public static boolean inRange(int x, int y, int N){
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    // 메인 로직
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        // 테스트 케이스 루프
        for (int t = 0; t < T; t++){
            
            int N = sc.nextInt();
            int M = sc.nextInt();

            // mat 대신, points와 flags 배열만으로 시뮬레이션 상태를 관리
            int[] directions = new int[M];
            int[][] points = new int[M][2];
            boolean[] flags = new boolean[M];

            // 방향 벡터 (0:R, 1:D, 2:L, 3:U)
            int[] dx = { 0, 1, 0, -1};
            int[] dy = { 1, 0, -1, 0};

            // 초기 입력 및 상태 설정
            for(int m = 0; m < M; m++){
                int i = sc.nextInt();
                int j = sc.nextInt();

                i--; j--; // 0-based 인덱스로 변환

                points[m][0] = i;
                points[m][1] = j;
                flags[m] = true;

                String direc = sc.next();
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
            // 문제 조건에 따라 시간 제한을 설정합니다. (예: 2*N, 1000 등)
            while (time < 2 * N){ 
                
                // 1단계: 모든 구슬의 다음 위치 계산 및 충돌 카운트 (O(M) + O(N^2))
                // 다음 시간 스텝의 위치별 구슬 개수를 세는 임시 배열
                int[][] nextMat = new int[N][N]; 
                
                for(int m = 0; m < M; m++){
                    if (!flags[m]) continue; // 소멸된 구슬은 건너뜀

                    int x = points[m][0];
                    int y = points[m][1];
                    int currentDirec = directions[m];

                    int nx = x + dx[currentDirec];
                    int ny = y + dy[currentDirec];

                    if (inRange(nx, ny, N)){
                        // (1-1) 다음 위치로 이동
                        points[m][0] = nx;
                        points[m][1] = ny;
                        nextMat[nx][ny] += 1; // 새 위치에서 충돌 카운트 증가

                    } else {
                        // (1-2) 벽에 부딪힘: 방향만 반대로 바꾸고 현재 위치 유지
                        currentDirec = (currentDirec + 2) % 4;
                        directions[m] = currentDirec;
                        nextMat[x][y] += 1; // 현재 위치에서 충돌 카운트 증가
                        // points[m]은 그대로 유지
                    } 
                }
                

                
                // 충돌 구슬 비활성화 (O(M))
                // M개의 구슬을 순회하며, 그 구슬이 충돌 지점에 있는지 확인
                for(int m = 0; m < M; m++){
                    if (flags[m]){
                        int x = points[m][0];
                        int y = points[m][1];
                        
                        // 충돌 리스트에 현재 구슬의 위치가 있는지 확인
                        // (충돌 리스트가 크지 않다면 O(N^2) < 50*50 = 2500 이므로 선형 탐색도 가능)
                        // 하지만 최악의 경우를 대비하여 Set을 사용하는 것이 가장 좋음.
                        // 여기서는 로직 단순화를 위해 충돌 좌표를 HashSet으로 관리하는 최적 코드를 제시합니다.
                        
                        // 충돌 구슬 비활성화는 1단계에서 얻은 nextMat 정보로만 진행됩니다.
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