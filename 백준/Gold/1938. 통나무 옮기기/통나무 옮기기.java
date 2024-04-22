import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, dx[] = { 0, 1, 0, -1 }, dy[] = { 1, 0, -1, 0 };
	static int dx2[] = { 0, 1, 1, 1, 0, -1, -1, -1 }, dy2[] = { 1, 1, 0, -1, -1, -1, 0, 1 };
	static int INF = Integer.MAX_VALUE;
	static int bx, by, ex, ey, ans = INF;
	static char[][] g;
	static boolean verB = false, verE = false, vis[][][];
	static Deque<Node> q = new ArrayDeque<>();

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		g = new char[n][n];
		boolean flagB = true, flagE = true;
		vis = new boolean[n][n][2];
		for (int i = 0; i < n; i++) {
			g[i] = br.readLine().toCharArray();
			for (int j = 0; j < n; j++) {
				if (g[i][j] == 'B' && flagB) {
					flagB = false;
					if (j < (n - 1) && g[i][j + 1] == 'B') {
						bx = i;
						by = j + 1;
					} else {
						bx = i + 1;
						by = j;
						verB = true;
					}
				}
				if (g[i][j] == 'E' && flagE) {
					flagE = false;
					if (j < (n - 1) && g[i][j + 1] == 'E') {
						ex = i;
						ey = j + 1;
					} else {
						ex = i + 1;
						ey = j;
						verE = true;
					}
				}
			}
		}
		solve();
		System.out.println(ans == INF ? 0 : ans);
	}

	static void solve() {
		q.offer(new Node(bx, by, 0, verB));
		vis[bx][by][verB ? 0 : 1] = true;
		bfs: while (!q.isEmpty()) {
			Node node = q.poll();
			int x = node.x;
			int y = node.y;
			int d = node.d;
			boolean b = node.b;
			if (x == ex && y == ey && b == verE) {
				ans = Math.min(ans, d);
				continue;
			}
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || n <= nx || ny < 0 || n <= ny)
					continue;
				if (b && (nx == 0 || nx == n - 1))
					continue;
				if (!b && (ny == 0 || ny == n - 1))
					continue;
				if (b && g[nx - 1][ny] != '1' && g[nx + 1][ny] != '1' && g[nx][ny] != '1' && !vis[nx][ny][0]) {
					vis[nx][ny][0] = true;
					q.offer(new Node(nx, ny, d + 1, b));
				}
				if (!b && g[nx][ny - 1] != '1' && g[nx][ny + 1] != '1' && g[nx][ny] != '1' && !vis[nx][ny][1]) {
					vis[nx][ny][1] = true;
					q.offer(new Node(nx, ny, d + 1, b));
				}
			}
			if (x == 0 || x == n - 1 || y == 0 || y == n - 1)
				continue bfs;
			for (int i = 0; i < 8; i++) {
				int nx = x + dx2[i];
				int ny = y + dy2[i];
				if (g[nx][ny] == '1')
					continue bfs;
			}
			if (!vis[x][y][b ? 1 : 0]) {
				vis[x][y][b ? 1 : 0] = true;
				q.offer(new Node(x, y, d + 1, !b));
			}
		}
	}

	static class Node {
		int x, y, d;
		boolean b;

		public Node(int x, int y, int d, boolean b) {
			this.x = x;
			this.y = y;
			this.d = d;
			this.b = b;
		}
	}
}