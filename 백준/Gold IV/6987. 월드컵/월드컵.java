import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
   static int[][] match; // 0: 승, 1: 무, 2: 패 정보 입력 받을 배열
   static boolean flag;

   public static void main(String[] args) throws IOException {

      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringBuilder sb = new StringBuilder();
      // 3개의 경기 결과 주어짐
      for (int m = 0; m < 4; m++) {
         match = new int[6][3];
         int sum = 0;
         StringTokenizer st = new StringTokenizer(br.readLine());
         for (int i = 0; i < 6; i++) { // 6개팀 경기 결과 입력
            sum += match[i][0] = Integer.parseInt(st.nextToken());
            sum += match[i][1] = Integer.parseInt(st.nextToken());
            sum += match[i][2] = Integer.parseInt(st.nextToken());
         }

         if (sum != 30) {// 총 15경기, 점수는 30점이 되어야 하는데 30점이 안되면 무조건 성립되지 않음.
            sb.append("0 ");
            continue;
         }

         flag = false;
         dfs(0,0,1);
         if (flag)
            sb.append("1 ");
         else
            sb.append("0 ");

      }
      System.out.println(sb);
   }


   static void dfs(int count, int t1, int t2) {
      if (flag)
         return; // 다른 dfs에서 조건을 만족했으면, 더이상 다른 탐색 진행할 필요 없으므로 return
      // 가지치기 안해도 O(3^15)으로 시간안에 들어옴
      if (count == 15) { // 경기 횟수가 15번이 됐으면, 경기가 성립된 것
         flag = true;
         return;
      }
      // 1. 경기 할 팀 2개 셋팅
      int nt1 = t1;
      int nt2 = t2 + 1;
      if (t2 == 5) {
         nt1 = t1 + 1;
         nt2 = nt1 + 1;
      }
      // 2. 3가지 경우에 다른 경기 해보기
      for (int m = 0; m < 3; m++) {// 승-패, 무-무, 패-승 경우 dfs 타기
         // 3. 정해진 경기 가능한지 받은 결과표에서 확인해보기
         if (match[t1][m] > 0 && match[t2][2 - m] > 0) {
            match[t1][m]--;
            match[t2][2 - m]--;
            // 다음 경기하러 가기
            dfs(count + 1, nt1, nt2);
            match[t1][m]++;
            match[t2][2 - m]++;
         }
      }
   }

}