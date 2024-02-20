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
	static int n, ans1, ans2;
	static int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };
	static char[][] g;
	static boolean[][] vis;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		g = new char[n][n];
		vis = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			g[i] = br.readLine().toCharArray();
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!vis[i][j]) {
					bfs(i, j, g[i][j]);
					ans1++;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (g[i][j] == 'G') {
					g[i][j] = 'R';
				}
			}
		}
		vis = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!vis[i][j]) {
					bfs(i, j, g[i][j]);
					ans2++;
				}
			}
		}
		System.out.println(ans1 + " " + ans2);
	}

	static void bfs(int x, int y, char c) {
		Deque<int[]> q = new ArrayDeque<int[]>();
		q.add(new int[] { x, y });
		vis[x][y] = true;
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int xx = tmp[0], yy = tmp[1];
			for (int i = 0; i < 4; i++) {
				int nx = xx + dx[i], ny = yy + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					if (!vis[nx][ny] && g[nx][ny] == c) {
						q.add(new int[] { nx, ny });
						vis[nx][ny] = true;
					}
				}
			}
		}
	}
}