/**
 * @author 이지원
 * @date 24.02.14
 * @link https://www.acmicpc.net/problem/6987
 * @keyword_solution 6팀의 조별리그는 총 15경기 필요
 * 모든 경기의 모든 결과(승, 무, 패)를 확인하여 유효성 판단
 * @input 4가지 경기 결과
 * @output 가능한 결과는 1, 불가능한 결과는 0 출력
 * @time_complex
 * @perf
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int[][] res = new int[6][3];
    static boolean flag;

    public static void main(String[] args) throws IOException {
        for (int t = 0; t < 4; t++) {
            st = new StringTokenizer(br.readLine());
            int total = 0;
            for (int i = 0; i < 6; i++) { // 6개팀 경기 결과 입력
                for (int j = 0; j < 3; j++) {
                    total += res[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 총 15경기이므로 전체 결과의 합은 30
            if (total != 30) {
                sb.append("0 ");
                continue;
            }
            flag = false;
            dfs(0, 0, 1);
            sb.append(flag ? 1 : 0).append(" ");
        }
        System.out.println(sb);
    }


    static void dfs(int count, int t1, int t2) {
        if (flag) {
            return; // 다른 dfs에서 조건을 만족했으면, 더이상 다른 탐색 진행할 필요 없으므로 return
            // 가지치기 안해도 O(3^15)으로 시간안에 들어옴
        }
        // 경기 횟수가 15번이 됐으면, 경기가 성립된 것
        if (count == 15) {
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
        for (int i = 0; i < 3; i++) {// 승-패, 무-무, 패-승 경우 dfs 타기
            // 3. 정해진 경기 가능한지 받은 결과표에서 확인해보기
            if (res[t1][i] > 0 && res[t2][2 - i] > 0) {
                res[t1][i]--;
                res[t2][2 - i]--;
                // 다음 경기하러 가기
                dfs(count + 1, nt1, nt2);
                res[t1][i]++;
                res[t2][2 - i]++;
            }
        }
    }
}