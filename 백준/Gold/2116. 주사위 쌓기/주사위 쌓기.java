import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, dice[][], ans = 0, side[] = { 5, 3, 4, 1, 2, 0 };

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		dice = new int[n][6];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 6; j++) {
				dice[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i < 6; i++) {
			dfs(0, 0, i, dice[0][i]);
		}
		System.out.println(ans);
	}

	static void dfs(int d, int total, int topIdx, int top) {
		if (d == n) {
			ans = Math.max(ans, total);
			return;
		}
		int nextTopIdx = 0;
		int nextTop = 0;
		if (d < n - 1) {
			for (int i = 0; i < 6; i++) {
				if (dice[d + 1][i] == top) {
					nextTopIdx = side[i];
					nextTop = dice[d + 1][nextTopIdx];
				}
			}
		}
		int maxSide = 0;
		for (int i = 0; i < 6; i++) {
			if (i != topIdx && i != side[topIdx]) {
				maxSide = Math.max(maxSide, dice[d][i]);
			}
		}
		dfs(d + 1, total + maxSide, nextTopIdx, nextTop);
	}
}