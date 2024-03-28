import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int R, C, answer = 1;
	static int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };
	static char[][] g;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		g = new char[R][C];
		for (int i = 0; i < R; i++) {
			String s = br.readLine();
			for (int j = 0; j < C; j++) {
				char c = s.charAt(j);
				g[i][j] = c;
			}
		}

		while (check()) {
			moveS();
			moveWater();
			answer++;
		}
		System.out.println("KAKTUS");
	}

	static void moveWater() {
		Deque<Node> q = new ArrayDeque<>();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] == '*')
					q.offer(new Node(i, j));
			}
		}
		while (!q.isEmpty()) {
			Node node = q.poll();
			int x = node.x, y = node.y;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (g[nx][ny] == 'S' || g[nx][ny] == '.') {
						g[nx][ny] = '*';
					}
				}
			}
		}
	}

	static void moveS() {
		Deque<Node> q = new ArrayDeque<>();
		Deque<Node> result = new ArrayDeque<>();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] == 'S')
					q.offer(new Node(i, j));
			}
		}
		while (!q.isEmpty()) {
			Node node = q.poll();
			int x = node.x, y = node.y;
			g[x][y] = '.';
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (g[nx][ny] == 'D') {
						System.out.println(answer);
						System.exit(0);
					}
					if (g[nx][ny] == '.') {
						result.offer(new Node(nx, ny));
					}
				}
			}
		}
		while (!result.isEmpty()) {
			Node node = result.poll();
			g[node.x][node.y] = 'S';
		}
	}

	static boolean check() {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] == 'S') {
					return true;
				}
			}
		}
		return false;
	}

	static class Node {
		int x;
		int y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}