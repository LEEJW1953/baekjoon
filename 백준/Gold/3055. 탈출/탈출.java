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
	static Deque<Node> water = new ArrayDeque<>();
	static Deque<Node> S = new ArrayDeque<>();

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
				if (c == 'S') {
					S.offer(new Node(i, j));
				}
				if (c == '*') {
					water.offer(new Node(i, j));
				}
			}
		}

		while (!S.isEmpty()) {
			moveWater();
			moveS();
			answer++;
		}
		System.out.println("KAKTUS");
	}

	static void moveWater() {
		int len = water.size();
		while (len-- > 0) {
			Node node = water.poll();
			for (int i = 0; i < 4; i++) {
				int nx = node.x + dx[i];
				int ny = node.y + dy[i];
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (g[nx][ny] == 'S' || g[nx][ny] == '.') {
						g[nx][ny] = '*';
						water.offer(new Node(nx, ny));
					}
				}
			}
		}
	}

	static void moveS() {
		int len = S.size();
		while (len-- > 0) {
			Node node = S.poll();
			for (int i = 0; i < 4; i++) {
				int nx = node.x + dx[i];
				int ny = node.y + dy[i];
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (g[nx][ny] == 'D') {
						System.out.println(answer);
						System.exit(0);
					}
					if (g[nx][ny] == '.') {
						g[nx][ny] = 'S';
						S.offer(new Node(nx, ny));
					}
				}
			}
		}
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