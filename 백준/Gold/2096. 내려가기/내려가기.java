import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //    static StringBuilder sb = new StringBuilder();
    static int INF = Integer.MAX_VALUE;
    static int n;
    static int[][] arr;
    static int[][][] dp;
    static int minn = INF;
    static int maxx = 0;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer((br.readLine()));
        n = Integer.parseInt(st.nextToken());
        arr = new int[n + 1][3];
        dp = new int[n + 1][3][2];

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 3; j++) {
                dp[i][j][1] = INF;
            }
        }

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][2] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                dp[1][i][j] = arr[1][i];
            }
        }
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 3; j++) {
                if (j == 0) {
                    dp[i][j][0] = Math.max(dp[i - 1][j][0] + arr[i][j], dp[i - 1][j + 1][0] + arr[i][j]);
                    dp[i][j][1] = Math.min(dp[i - 1][j][1] + arr[i][j], dp[i - 1][j + 1][1] + arr[i][j]);
                } else if (j == 1) {
                    dp[i][j][0] = Math.max(dp[i - 1][j - 1][0] + arr[i][j], dp[i - 1][j][0] + arr[i][j]);
                    dp[i][j][0] = Math.max(dp[i][j][0], dp[i - 1][j + 1][0] + arr[i][j]);
                    dp[i][j][1] = Math.min(dp[i - 1][j - 1][1] + arr[i][j], dp[i - 1][j][1] + arr[i][j]);
                    dp[i][j][1] = Math.min(dp[i][j][1], dp[i - 1][j + 1][1] + arr[i][j]);
                } else {
                    dp[i][j][0] = Math.max(dp[i - 1][j][0] + arr[i][j], dp[i - 1][j - 1][0] + arr[i][j]);
                    dp[i][j][1] = Math.min(dp[i - 1][j][1] + arr[i][j], dp[i - 1][j - 1][1] + arr[i][j]);
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            minn = Math.min(minn, dp[n][i][1]);
            maxx = Math.max(maxx, dp[n][i][0]);
        }
        System.out.println(maxx + " " + minn);
    }
}