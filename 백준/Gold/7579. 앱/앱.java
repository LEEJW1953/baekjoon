import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, m[], c[], total, ans = Integer.MAX_VALUE;
	static int[][][] dp;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		m = new int[N + 1];
		c = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			m[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			int num = Integer.parseInt(st.nextToken());
			c[i] = num;
			total += num;
		}
		dp = new int[N + 1][total + 1][2];
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j <= total; j++) {
				if (j - c[i] >= 0) {
					int prev = dp[i - 1][j][0];
					int curr = dp[i - 1][j - c[i]][0] + m[i];
					if (prev < curr) {
						dp[i][j][0] = curr;
						dp[i][j][1] = dp[i - 1][j - c[i]][1] + c[i];
					} else {
						dp[i][j][0] = dp[i - 1][j][0];
						dp[i][j][1] = dp[i - 1][j][1];
					}
				} else {
					dp[i][j][0] = dp[i - 1][j][0];
					dp[i][j][1] = dp[i - 1][j][1];
				}
			}
		}
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= total; j++) {
				if (dp[i][j][0] >= M) {
					ans = Math.min(ans, dp[i][j][1]);
				}
			}
		}
		System.out.println(ans);
	}
}