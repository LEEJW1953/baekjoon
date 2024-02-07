import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int INF = Integer.MAX_VALUE;
	static int n, m, r;
	static int[][] g;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		g = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				g[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < r; i++) {
			round(Integer.parseInt(st.nextToken()));
		}
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[0].length; j++) {
				System.out.print(g[i][j] + " ");
			}
			System.out.println();
		}
	}

	static void round(int r) {
		int[][] tmp;
		n = g.length;
		m = g[0].length;
		switch (r) {
		case 1:
			tmp = new int[n][m];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					tmp[i][j] = g[n - 1 - i][j];
				}
			}
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		case 2:
			tmp = new int[n][m];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					tmp[i][j] = g[i][m - 1 - j];
				}
			}
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		case 3:
			tmp = new int[m][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					tmp[j][n - 1 - i] = g[i][j];
				}
			}
			g = new int[m][n];
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		case 4:
			tmp = new int[m][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					tmp[m - 1 - j][i] = g[i][j];
				}
			}
			g = new int[m][n];
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		case 5:
			tmp = new int[n][m];
			int[][] clockwise = new int[][] { { 0, 0 }, { 0, m / 2 }, { n / 2, m / 2 }, { n / 2, 0 } };
			for (int k = 0; k < 4; k++) {
				int x = clockwise[k][0];
				int y = clockwise[k][1];
				int tx = clockwise[(k + 1) % 4][0];
				int ty = clockwise[(k + 1) % 4][1];
				for (int i = 0; i < n / 2; i++) {
					for (int j = 0; j < m / 2; j++) {
						tmp[tx + i][ty + j] = g[x + i][y + j];
					}
				}
			}
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		case 6:
			tmp = new int[n][m];
			int[][] counterClockwise = new int[][] { { 0, 0 }, { n / 2, 0 }, { n / 2, m / 2 }, { 0, m / 2 } };
			for (int k = 0; k < 4; k++) {
				int x = counterClockwise[k][0];
				int y = counterClockwise[k][1];
				int tx = counterClockwise[(k + 1) % 4][0];
				int ty = counterClockwise[(k + 1) % 4][1];
				for (int i = 0; i < n / 2; i++) {
					for (int j = 0; j < m / 2; j++) {
						tmp[tx + i][ty + j] = g[x + i][y + j];
					}
				}
			}
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					g[i][j] = tmp[i][j];
				}
			}
			break;
		default:
			break;
		}
	}
}