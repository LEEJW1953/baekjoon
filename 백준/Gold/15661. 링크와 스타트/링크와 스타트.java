import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static int[][] g;
    static boolean[] vis;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        g = new int[n][n];
        vis = new boolean[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int t = 1; t <= n / 2; t++) {
            for (int i = 0; i < n; i++) {
                vis[i] = true;
                solve(i, t, 1);
                vis[i] = false;
            }
        }

        System.out.println(ans / 2);
    }

    public static void solve(int cur, int t, int d) {
        if (d == t) {
            int t1 = 0;
            int t2 = 0;
            for (int k = 0; k < n; k++) {
                for (int j = 0; j < n; j++) {
                    if (vis[k] && vis[j]) {
                        t1 += g[k][j] + g[j][k];
                    }
                    if (!vis[k] && !vis[j]) {
                        t2 += g[k][j] + g[j][k];
                    }
                }
            }
            ans = Math.min(ans, Math.abs(t1 - t2));
            if (ans == 0) {
                System.out.println(0);
                System.exit(0);
            }
            return;
        }
        for (int i = cur + 1; i < n; i++) {
            vis[i] = true;
            solve(i, t, d + 1);
            vis[i] = false;
        }
    }
}