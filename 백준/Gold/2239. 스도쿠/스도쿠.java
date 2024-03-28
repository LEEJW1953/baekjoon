import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static int[][] g = new int[9][9];
	static int[] row = new int[9];
	static int[] col = new int[9];
	static int[] square = new int[9];
	static int[] log = new int[513];

	public static void main(String[] args) throws Exception {
		for (int i = 0; i < 9; i++) {
			String s = br.readLine();
			for (int j = 0; j < 9; j++) {
				int num = s.charAt(j) - '0';
				g[i][j] = num;
				if (num != 0) {
					row[i] |= 1 << num;
					col[j] |= 1 << num;
					square[(i / 3) * 3 + (j / 3)] |= 1 << num;
				}
			}
		}
		for (int i = 1; i <= 9; i++) {
			log[1 << i] = i;
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
			int used = row[x] | col[y] | square[block];
			int num = 1 << i;
			if ((num & used) != num) {
				g[x][y] = log[num];
				row[x] |= num;
				col[y] |= num;
				square[block] |= num;
				dfs(d + 1);
				g[x][y] = 0;
				row[x] &= ~num;
				col[y] &= ~num;
				square[block] &= ~num;
			}
		}
	}
}