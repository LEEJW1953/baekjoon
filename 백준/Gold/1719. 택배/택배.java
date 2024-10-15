import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    //    static StringBuilder sb = new StringBuilder();
    static int n, m;
    static int[][][] vis;
    static int INF = 200000000;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        vis = new int[n + 1][n + 1][2];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                vis[i][j] = new int[]{0, INF};
                if (i == j) {
                    vis[i][j][1] = 0;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (c < vis[a][b][1]) {
                vis[a][b][0] = b;
                vis[a][b][1] = c;
                vis[b][a][0] = a;
                vis[b][a][1] = c;
            }
        }
        for (int k = 1; k <= n; k++) {
            for (int j = 1; j <= n; j++) {
                for (int i = 1; i <= n; i++) {
                    int cost = vis[i][k][1] + vis[k][j][1];
                    if (cost < vis[i][j][1]) {
                        vis[i][j][1] = cost;
                        vis[i][j][0] = vis[i][k][0] == 0 ? k : vis[i][k][0];
                    }
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                int k = vis[i][j][0];
                while (true) {
                    if (k == vis[i][k][0]) {
                        break;
                    }
                    k = vis[i][k][0] == 0 ? k : vis[i][k][0];
                }
                vis[i][j][0] = k;
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j || vis[i][j][0] == 0) {
                    System.out.print("-" + " ");
                } else {
                    System.out.print(vis[i][j][0] + " ");
                }
            }
            System.out.println();
        }
    }
}