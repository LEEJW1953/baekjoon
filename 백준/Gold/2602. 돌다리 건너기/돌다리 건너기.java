import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[] c, u, d;
	static int[][][] dp;
	static int n, m, ans = 0;

	public static void main(String[] args) throws Exception {
		c = br.readLine().toCharArray();
		u = br.readLine().toCharArray();
		d = br.readLine().toCharArray();
		n = u.length;
		m = c.length;
		dp = new int[2][n][m];
		for (int i = 0; i < n; i++) {
			if (c[0] == u[i]) {
				dp[0][i][0]++;
			}
			if (c[0] == d[i]) {
				dp[1][i][0]++;
			}
			for (int j = 0; j < i; j++) {
				for (int k = 0; k < m - 1; k++) {
					int count = dp[0][j][k];
					if (count > 0 && c[k + 1] == d[i]) {
						dp[1][i][k + 1] += count;
					}
				}
				for (int k = 0; k < m - 1; k++) {
					int count = dp[1][j][k];
					if (count > 0 && c[k + 1] == u[i]) {
						dp[0][i][k + 1] += count;
					}
				}
			}
			ans += dp[0][i][m - 1];
			ans += dp[1][i][m - 1];
		}
		System.out.println(ans);
	}
}