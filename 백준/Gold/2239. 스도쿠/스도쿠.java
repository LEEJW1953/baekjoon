import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
//	static StringTokenizer st;
	static int[][] g = new int[9][9];
	static boolean[][] row = new boolean[9][10];
	static boolean[][] col = new boolean[9][10];
	static boolean[][] square = new boolean[9][10];

	public static void main(String[] args) throws Exception {
		for (int i = 0; i < 9; i++) {
			String s = br.readLine();
			for (int j = 0; j < 9; j++) {
				int num = s.charAt(j) - '0';
				g[i][j] = num;
				if (num != 0) {
					row[i][num] = true;
					col[j][num] = true;
					square[(i / 3) * 3 + (j / 3)][num] = true;
				}
			}
		}
		dfs(0);
	}

	static void dfs(int d) {
		if (d == 81) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sb.append(g[i][j]);
				}
				sb.append("\n");
			}
			System.out.println(sb);
			System.exit(0);
		}
		int x = d / 9;
		int y = d % 9;
		if (g[x][y] != 0) {
			dfs(d + 1);
			return;
		}
		int block = (x / 3) * 3 + (y / 3);
		for (int i = 1; i <= 9; i++) {
			if (!row[x][i] && !col[y][i] && !square[block][i]) {
				g[x][y] = i;
				row[x][i] = true;
				col[y][i] = true;
				square[block][i] = true;
				dfs(d + 1);
				g[x][y] = 0;
				row[x][i] = false;
				col[y][i] = false;
				square[block][i] = false;
			}
		}
	}
}