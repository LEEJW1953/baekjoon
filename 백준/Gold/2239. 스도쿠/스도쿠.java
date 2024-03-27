import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author 이지원
 * @date 24.03.27
 * @link
 * @keyword_solution
 * @input
 * @output
 * @time_complex
 * @perf
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static List<int[]> blank = new ArrayList<>();
	static int[][] g = new int[9][9];

	public static void main(String[] args) throws Exception {
		for (int i = 0; i < 9; i++) {
			String s = br.readLine();
			for (int j = 0; j < 9; j++) {
				int num = s.charAt(j) - '0';
				g[i][j] = num;
				if (num == 0)
					blank.add(new int[] { i, j });
			}
		}
		dfs(0);
	}

	static void dfs(int d) {
		if (d == blank.size()) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sb.append(g[i][j]);
				}
				sb.append("\n");
			}
			System.out.println(sb);
			System.exit(0);
		}
		for (int i = 1; i <= 9; i++) {
			int x = blank.get(d)[0];
			int y = blank.get(d)[1];
			if (hor(i, x) && ver(i, y) && square(i, x, y)) {
				g[x][y] = i;
				dfs(d + 1);
				g[x][y] = 0;
			}
		}
	}

	static boolean hor(int num, int x) {
		for (int i = 0; i < 9; i++) {
			if (g[x][i] == num) {
				return false;
			}
		}
		return true;
	}

	static boolean ver(int num, int y) {
		for (int i = 0; i < 9; i++) {
			if (g[i][y] == num) {
				return false;
			}
		}
		return true;
	}

	static boolean square(int num, int x, int y) {
		int startX = 3 * (x / 3);
		int startY = 3 * (y / 3);
		for (int i = startX; i < startX + 3; i++) {
			for (int j = startY; j < startY + 3; j++) {
				if (g[i][j] == num) {
					return false;
				}
			}
		}
		return true;
	}
}