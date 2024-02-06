import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, r;
	static int[][] arr;
	static int[][] ans;
	static int[] dx = new int[] { 1, 0, -1, 0 };
	static int[] dy = new int[] { 0, 1, 0, -1 };

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		ans = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int c = Math.min(n, m) / 2;
		for (int i = 0; i < c; i++) {
			rotate(i);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(ans[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	static void rotate(int x) {
		int round = 2 * (n + m) - 8 * x - 4;
		int count = r % round;
		List<int[]> coords = new ArrayList<>();
		int row = n - 1 - 2 * x;
		int col = m - 1 - 2 * x;
		for (int i = 0; i < round; i++) {
			if (0 <= i && i < row) {
				coords.add(new int[] { x + i, x });
			} else if (i < row + col) {
				coords.add(new int[] { x + row, x + i - row });
			} else if (i < 2 * row + col) {
				coords.add(new int[] { x + 2 * row + col - i, x + col });
			} else {
				coords.add(new int[] { x, x + 2 * (col + row) - i });
			}
		}
		for (int i = 0; i < round; i++) {
			int idx = (i + count) % round;
			ans[coords.get(idx)[0]][coords.get(idx)[1]] = arr[coords.get(i)[0]][coords.get(i)[1]];
		}
	}
}