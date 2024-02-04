/**
 * @author 이지원
 * @date 24.01.31
 * @link https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY0LFFoqrIIDFAXz&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AY0LFFoqrIMDFAXz+&type=PROBLEM&problemBoxTitle=0129%EC%A3%BC&problemBoxCnt=++6+
 * @keyword_solution 이차원 베열을 순회하며 한 칸씩 숫자를 채운다
 * @input 첫 줄에는 테스트 케이스의 수 T, 그 아래 T개의 줄에 달팽이의 크기 N
 * @output 달팽이 숫자의 이차원 배열 출력
 * @time_complex O(n ^ 2)
 * @perf
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n;
    static int ans = 0;
    static List<Integer> queens = new ArrayList<>(); // index 가 퀸의 x좌표, 값이 y좌표

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        queen(0);
        System.out.println(ans);
    }

    static void queen(int x) {
        if (x == n) {
            ans++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (check(i)) {
                queens.add(i);
                queen(x + 1);
                queens.remove(queens.size() - 1);
            }
        }
    }

    static boolean check(int x) {
        int s = queens.size();
        for (int i = 0; i < s; i++) {
            int q = queens.get(i);
            if (q == x || (i - q) == (s - x) || (i + q) == (s + x)) {
                return false;
            }
        }
        return true;
    }
}