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
	static int n, m, g[][], time = 0, size;
	static int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int num = Integer.parseInt(st.nextToken());
				g[i][j] = num;
				size += num;
			}
		}
		while (true) {
			time++;
			int tmp = bfs();
			if (tmp == 0) {
				break;
			}
			size = tmp;
		}
		System.out.println(time);
		System.out.println(size);
	}

	static int bfs() {
		Deque<int[]> q = new ArrayDeque<int[]>();
		boolean[][] vis = new boolean[n][m];
		int[][] arr = new int[n][m];
		q.add(new int[] { 0, 0 });
		vis[0][0] = true;
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int x = tmp[0], y = tmp[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m) {
					if (!vis[nx][ny]) {
						if (g[nx][ny] == 0) {
							q.add(new int[] { nx, ny });
						}
						arr[nx][ny] = g[nx][ny];
						vis[nx][ny] = true;
					}
				}
			}
		}
		int size = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				g[i][j] -= arr[i][j];
				size += g[i][j];
			}
		}
		return size;
	}
}