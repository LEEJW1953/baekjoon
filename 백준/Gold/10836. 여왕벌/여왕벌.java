import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int m, n, g[][];

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		g = new int[m][m];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < m; j++) {
				g[i][j] = 1;
			}
		}
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			solve(a, b, c);
		}
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(g[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	static void solve(int a, int b, int c) {
		int count = 2 * m - 1;
		int[] arr = new int[count];
		for (int i = 0; i < count; i++) {
			if (a > 0) {
				arr[i] = 0;
				a--;
			} else if (b > 0) {
				arr[i] = 1;
				b--;
			} else if (c > 0) {
				arr[i] = 2;
				c--;
			}
		}
		int x = m - 1, y = 0;
		int tmp[][] = new int[m][m];
		for (int i = 0; i < count; i++) {
			g[x][y] += arr[i];
			tmp[x][y] = arr[i];
			if (x > 0) {
				x--;
			} else {
				y++;
			}
		}
		for (int i = 1; i < m; i++) {
			for (int j = 1; j < m; j++) {
				int num = Math.max(tmp[i - 1][j - 1], Math.max(tmp[i][j - 1], tmp[i - 1][j]));
				tmp[i][j] = num;
				g[i][j] += num;
			}
		}
	}
}