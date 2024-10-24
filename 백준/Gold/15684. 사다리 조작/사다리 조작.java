import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, h;
    static boolean[][] ladder;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        ladder = new boolean[h][n];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            ladder[a - 1][b - 1] = true;
        }
        for (int i = 0; i < 4; i++) {
            solve(0, i, 0);
        }
        System.out.println(-1);
    }

    static void solve(int x, int k, int a) {
        if (x > k) {
            return;
        }
        if (x == k) {
            if (check()) {
                System.out.println(x);
                System.exit(0);
            } else {
                return;
            }
        }
        for (int i = a; i < h; i++) {
            for (int j = 0; j < n; j++) {
                if (j == n - 1 && !ladder[i][j - 1]) {
                    ladder[i][j - 1] = true;
                    solve(x + 1, k, i);
                    ladder[i][j - 1] = false;
                } else if (j == 0 && !ladder[i][j]) {
                    ladder[i][j] = true;
                    solve(x + 1, k, i);
                    ladder[i][j] = false;
                } else if (0 < j && j < n - 1 && !ladder[i][j - 1] && !ladder[i][j]) {
                    ladder[i][j] = true;
                    solve(x + 1, k, i);
                    ladder[i][j] = false;
                }
            }
        }
    }

    static boolean check() {
        for (int i = 0; i < n; i++) {
            int num = i;
            for (int j = 0; j < h; j++) {
                if (num < n && ladder[j][num]) {
                    num++;
                } else if (0 < num && ladder[j][num - 1]) {
                    num--;
                }
            }
            if (num != i) {
                return false;
            }
        }
        return true;
    }
}