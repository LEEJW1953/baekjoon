import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int R, C, T, g[][], x1, x2, ans = 0;
	static int[] dx1 = { 0, -1, 0, 1 }, dy = { 1, 0, -1, 0 };
	static int[] dx2 = { 0, 1, 0, -1 };

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		g = new int[R][C];
		boolean flag = false;
		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < C; j++) {
				int num = Integer.parseInt(st.nextToken());
				g[i][j] = num;
				if (num == -1) {
					if (!flag) {
						x1 = i;
						flag = true;
					} else {
						x2 = i;
					}
				}
			}
		}
		for (int i = 0; i < T; i++) {
			spread();
			rotate(false);
			rotate(true);
		}
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] > 0) {
					ans += g[i][j];
				}
			}
		}
		System.out.println(ans);
	}

	static void spread() {
		int[][] board = new int[R][C];
		board[x1][0] = -1;
		board[x2][0] = -1;
		Deque<Node> q = new ArrayDeque<>();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] > 0) {
					q.offer(new Node(i, j));
				}
			}
		}
		while (!q.isEmpty()) {
			Node node = q.poll();
			int x = node.x, y = node.y;
			int count = 0;
			int tmp = g[x][y] / 5;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx1[i], ny = y + dy[i];
				if (0 <= nx && nx < R && 0 <= ny && ny < C) {
					if (g[nx][ny] != -1) {
						board[nx][ny] += tmp;
						count++;
					}
				}
			}
			board[x][y] += (g[x][y] - (count * tmp));
		}
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				g[i][j] = board[i][j];
			}
		}
	}

	static void rotate(boolean b) {
		int startX = b ? x1 : x2;
		int startY = 0;
		int x = b ? x1 : x2;
		int y = 0;
		int[] dx = b ? dx1 : dx2;
		int idx = 0;
		int nx;
		int ny;
		int tmp = g[x][y];
		int tmp1;
		while (true) {
			nx = x + dx[idx];
			ny = y + dy[idx];
			if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
				idx = (idx + 1) % 4;
				nx = x + dx[idx];
				ny = y + dy[idx];
			}
			if (nx == startX && ny == startY) {
				break;
			}
			tmp1 = g[nx][ny];
			if (tmp == -1) {
				g[nx][ny] = 0;
			} else {
				g[nx][ny] = tmp;
			}
			tmp = tmp1;
			x = nx;
			y = ny;
		}
	}

	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}