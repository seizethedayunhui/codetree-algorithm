import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];

        boolean flag = false;

        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();

            if (arr[i] > 0){
                flag = true;
            }
        }

        // 최댓값이 나오기 위해서는
        // + + + 을 3개 곱하기 (내림차순 3개 선택)

        int posNum1 = Integer.MIN_VALUE;
        int posNum2 = Integer.MIN_VALUE;
        int posNum3 = Integer.MIN_VALUE;

        int posIdx1 = Integer.MIN_VALUE;
        int posIdx2 = Integer.MIN_VALUE;

        for (int i = 0; i < 3; i++){

            if (i == 0){
                for (int j = 0; j < N; j++){

                    if (arr[j] >= posNum1){
                        posNum1 = arr[j];
                        posIdx1 = j;
                    }

                }
            } else if (i == 1){
                for (int j = 0; j < N; j++){             
                    if (arr[j] <= posNum1 && arr[j] > posNum2 && j != posIdx1){
                        posNum2 = arr[j];
                        posIdx2 = j;
                    }
                }
            } else {
                for(int j = 0; j < N ; j++){
                    if (arr[j] <= posNum1 && arr[j] <= posNum2 && arr[j] > posNum3 && posIdx1 != j && posIdx2 != j ){
                        posNum3 = arr[j];
                    }
                }
            }

            // System.out.println(posNum1 + ", " + posNum2 + ", " + posNum3);
        }

        int maxMul1 = posNum1 * posNum2 * posNum3;

        // - - + 를 3개 곱하기 (음수 오름차순 2개, 양수 내림차순 1개)

        int negNum1 = Integer.MAX_VALUE;
        int negNum2 = Integer.MAX_VALUE;

        int negIdx1 = Integer.MIN_VALUE;
        int negIdx2 = Integer.MIN_VALUE;

        for (int i = 0; i < 2; i++){

                if (i == 0){
                    for (int j = 0; j < N; j++){
                        if (arr[j] < 0){
                            negNum1 = Math.min(negNum1, arr[j]);
                            negIdx1 = j;
                        }
                    }
                } else {
                    for(int j = 0; j < N ; j++){

                        if (arr[j] < 0){
                            if (arr[j] >= negNum1 && arr[j] < negNum2 && negIdx1 != j){
                                negNum2 = arr[j];
                            }
                        }
                    }
                }


        }

        int maxMul2 = negNum1 * negNum2 * posNum1 ;

        int ans = (flag) ? Math.max(maxMul1, maxMul2) : maxMul1 ;
        // System.out.println(maxMul1 + ", " + maxMul2);
        // System.out.println(posNum1 + ", " + posNum2 + ", " + posNum3);
        System.out.println(ans);

    }
}
