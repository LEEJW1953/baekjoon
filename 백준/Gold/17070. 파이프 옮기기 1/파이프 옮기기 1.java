import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, g[][], dp[][][], ans;

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		g = new int[n][n];
		dp = new int[n][n][3];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				g[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dp[0][1][0] = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				// 가로 이동
				int x = i, y = j + 1;
				if (x < n && y < n) {
					if (g[x][y] == 0) {
						dp[x][y][0] += dp[i][j][0] + dp[i][j][2];
					}
				}
				// 세로 이동
				x = i + 1;
				y = j;
				if (x < n && y < n) {
					if (g[x][y] == 0) {
						dp[x][y][1] += dp[i][j][1] + dp[i][j][2];
					}
				}
				// 대각선 이동
				x = i + 1;
				y = j + 1;
				if (x < n && y < n) {
					if (g[x][j] == 0 && g[i][y] == 0 && g[x][y] == 0) {
						dp[x][y][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2];
					}
				}
			}
		}
		for (int i = 0; i < 3; i++) {
			ans += dp[n - 1][n - 1][i];
		}
		System.out.println(ans);
	}
}