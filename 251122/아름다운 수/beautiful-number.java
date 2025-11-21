import java.util.*;

public class Main {

    public static ArrayList<Integer> beautifulNum = new ArrayList<>();
    public static int cnt;
    public static void makeNum(int N) {

        if ( N == 0 ) {
            isBeautifulNum(beautifulNum, 0, beautifulNum.get(0), beautifulNum.size(), 0);
            return;
        }

        for(int i = 1; i < 5; i++){
            beautifulNum.add(i);
            makeNum(N-1);
            beautifulNum.remove(beautifulNum.size()-1);
        }

        return;
    }

    public static void isBeautifulNum(ArrayList<Integer> beautifulNum, int idx, int element, int N, int currentCnt){

        if (idx == N) {
            if(element != currentCnt){
                //System.out.println("들어왔어요");
                return;
            }
            //System.out.println("들어옴");
            // for(int k : beautifulNum){
            //     System.out.print(k+" ");
            // }
            // System.out.println();
            cnt++;
            return;
        }

        int e = beautifulNum.get(idx);

        if ( currentCnt == e ) currentCnt = 0;

        if (element == e){
            currentCnt++;
        } else {

            if(element != currentCnt){
                //System.out.println("들어왔어요");
                return;
            }

            element = e;
            currentCnt = 1;
        }
        //System.out.println(e +", " + element +", " + currentCnt);
        idx += 1;
        isBeautifulNum(beautifulNum, idx, element, N, currentCnt);
    
        return;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        makeNum(N);
        System.out.println(cnt);

    }
}