import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int[][] rgb;
	static int[][] dp;
	static int ans = 10000000;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		rgb = new int[n][3];
		dp = new int[n + 1][3];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				rgb[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int k = 0; k < 3; k++) {
			int h1 = k % 3;
			int h2 = (k + 1) % 3;
			int h3 = (k + 2) % 3;
			dp[1][h1] = rgb[0][h1];
			dp[1][h2] = 10000000;
			dp[1][h3] = 10000000;
			for (int i = 2; i <= n; i++) {
				for (int j = 0; j < 3; j++) {
					int r1 = (j + 1) % 3;
					int r2 = (j + 2) % 3;
					dp[i][j] = Math.min(dp[i - 1][r1], dp[i - 1][r2]) + rgb[i - 1][j];
				}
			}
			ans = (Math.min(ans, Math.min(dp[n][h2], dp[n][h3])));
		}

		System.out.println(ans);
	}
}