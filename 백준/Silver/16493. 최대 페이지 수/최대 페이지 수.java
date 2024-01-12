import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[m][2];
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i < m; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st1.nextToken());
            int b = Integer.parseInt(st1.nextToken());
            arr[i][0] = a;
            arr[i][1] = b;
        }

        for (int i = 1; i < m + 1; i++) {
            int cost = arr[i - 1][0];
            for (int j = 1; j < n + 1; j++) {
                if (cost<=j){
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - cost] + arr[i - 1][1]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        System.out.println(dp[m][n]);
    }
}