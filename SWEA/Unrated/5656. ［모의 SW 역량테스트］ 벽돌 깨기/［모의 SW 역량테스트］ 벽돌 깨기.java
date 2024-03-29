import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, ans, n, w, h, g[][], hit[];
	static int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws Exception {
		T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			ans = Integer.MAX_VALUE;
			n = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			g = new int[h][w];
			hit = new int[n];
			for (int i = 0; i < h; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < w; j++) {
					g[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			for (int j = 0; j < w; j++) {
				for (int i = 0; i < h; i++) {
					if (g[i][j] != 0) {
						play(i, j, 0, g);
						break;
					}
				}
			}
			sb.append("#" + t + " " + ans).append("\n");
		}
		System.out.println(sb);
	}

	static void play(int x, int y, int d, int[][] board) {
		if (d == n) {
			int total = 0;
			for (int j = 0; j < w; j++) {
				for (int i = 0; i < h; i++) {
					if (board[i][j] != 0) {
						total++;
					}
				}
			}
			ans = Math.min(ans, total);
			return;
		}

		int[][] tmp = new int[h][w];
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				tmp[i][j] = board[i][j];
			}
		}

		// 폭탄 터뜨리기
		Deque<Node> q = new ArrayDeque<>();
		q.offer(new Node(x, y));
		while (!q.isEmpty()) {
			Node node = q.poll();
			int curX = node.x, curY = node.y;
			int power = tmp[curX][curY];
			tmp[curX][curY] = 0;
			for (int k = 0; k < 4; k++) {
				for (int l = 0; l < power; l++) {
					int nx = curX + dx[k] * l;
					int ny = curY + dy[k] * l;
					if (0 <= nx && nx < h && 0 <= ny && ny < w) {
						if (tmp[nx][ny] > 0) {
							q.offer(new Node(nx, ny));
						}
					}
				}
			}
		}

		// 바닥으로 내림
		int total = 0;
		for (int i = 0; i < w; i++) {
			int idx = h - 1;
			for (int j = h - 1; j >= 0; j--) {
				if (tmp[j][i] != 0) {
					int num = tmp[j][i];
					tmp[j][i] = 0;
					tmp[idx--][i] = num;
					total++;
				}
			}
		}
		if (total == 0) {
			ans = 0;
			return;
		}

		// 다음 폭탄
		for (int j = 0; j < w; j++) {
			for (int i = 0; i < h; i++) {
				if (tmp[i][j] != 0) {
					play(i, j, d + 1, tmp);
					break;
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