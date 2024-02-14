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
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int idx = 0, res[][] = new int[6][3], game[][] = new int[15][2];

    public static void main(String[] args) throws IOException {
        // 전체 경기 경우의 수
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) {
                game[idx][0] = i;
                game[idx++][1] = j;
            }
        }

        loop:
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            int total = 0;
            for (int j = 0; j < 6; j++) {
                for (int k = 0; k < 3; k++) {
                    int num = Integer.parseInt(st.nextToken());
                    res[j][k] = num;
                    total += num;
                }
            }
            // 총 15경기이므로 전체 결과의 합은 30
            if (total != 30) {
                sb.append(0 + " ");
                continue;
            }
            sb.append(dfs(0) ? 1 : 0).append(" ");
        }
        System.out.println(sb);
    }

    static boolean dfs(int d) {
        if (d == 15) {
            return true;
        }
        // 이번 경기를 하는 두 팀
        int team1 = game[d][0];
        int team2 = game[d][1];
        // 1팀 승리
        if (0 <= --res[team1][0] & 0 <= --res[team2][2]) {
            if (dfs(d + 1)) {
                return true;
            }
        }
        res[team1][0]++;
        res[team2][2]++;
        // 무승부
        if (0 <= --res[team1][1] & 0 <= --res[team2][1]) {
            if (dfs(d + 1)) {
                return true;
            }
        }
        res[team1][1]++;
        res[team2][1]++;
        // 2팀 승리
        if (0 <= --res[team1][2] & 0 <= --res[team2][0]) {
            if (dfs(d + 1)) {
                return true;
            }
        }
        res[team1][2]++;
        res[team2][0]++;
        return false;
    }
}