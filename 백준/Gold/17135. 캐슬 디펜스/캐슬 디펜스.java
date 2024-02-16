import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, d, g[][], ans = 0, archer[] = new int[3], enemy;
	static int[] dx = { 0, -1, 0, 1 }, dy = { -1, 0, 1, 0 };

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		g = new int[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int num = Integer.parseInt(st.nextToken());
				g[i][j] = num;
				if (num == 1) {
					enemy++;
				}
			}
		}
		archer = new int[] { 0, 1, 2 };
		for (int i = 0; i < m; i++) {
			for (int j = i + 1; j < m; j++) {
				for (int k = j + 1; k < m; k++) {
					archer[0] = i;
					archer[1] = j;
					archer[2] = k;
					game();
				}
			}
		}
		System.out.println(ans);
	}

	static void game() {
		int[][] tmp = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				tmp[i][j] = g[i][j];
			}
		}
		int enemyCount = enemy;
		int count = 0;
		while (0 < enemyCount) {
			Deque<int[]> kill = new ArrayDeque<int[]>();

			for (int x : archer) {
				int[] res = bfs(n, x, tmp);
				if (res != null) {
					kill.add(res);
				}
			}

			while (!kill.isEmpty()) {
				int[] target = kill.poll();
				if (tmp[target[0]][target[1]] == 1) {
					tmp[target[0]][target[1]] = 0;
					count++;
				}
			}

			for (int i = n - 1; i > 0; i--) {
				for (int j = 0; j < m; j++) {
					tmp[i][j] = tmp[i - 1][j];
				}
			}
			for (int j = 0; j < m; j++) {
				tmp[0][j] = 0;
			}

			enemyCount = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (tmp[i][j] == 1) {
						enemyCount++;
					}
				}
			}
		}
		ans = Math.max(ans, count);
	}

	static int[] bfs(int x, int y, int[][] board) {
		Deque<int[]> q = new ArrayDeque<int[]>();
		boolean[][] vis = new boolean[n][m];
		q.offer(new int[] { x, y, 0 });
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int xx = tmp[0], yy = tmp[1], dd = tmp[2];
			for (int i = 0; i < 4; i++) {
				int nx = xx + dx[i], ny = yy + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m) {
					if (!vis[nx][ny] && dd < d) {
						if (board[nx][ny] == 1) {
							return new int[] { nx, ny };
						}
						q.offer(new int[] { nx, ny, dd + 1 });
						vis[nx][ny] = true;
					}
				}
			}
		}
		return null;
	}
}