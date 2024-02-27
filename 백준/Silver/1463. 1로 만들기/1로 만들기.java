import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, dp[];

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		dp = new int[N + 1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		dp[N] = 0;
		for (int i = N; i > 1; i--) {
			if (i % 3 == 0) {
				int x = i / 3;
				dp[x] = Math.min(dp[x], dp[i] + 1);
			}
			if (i % 2 == 0) {
				int x = i / 2;
				dp[x] = Math.min(dp[x], dp[i] + 1);
			}
			dp[i - 1] = Math.min(dp[i - 1], dp[i] + 1);
		}
		System.out.println(dp[1]);
	}
}