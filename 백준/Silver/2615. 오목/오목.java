import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int[][] g = new int[19][19];
	static int[] dx = { 0, 1, 1, -1 };
	static int[] dx1 = { 0, -1, -1, 1 };
	static int[] dy = { 1, 0, 1, 1 };
	static int[] dy1 = { -1, 0, -1, -1 };
	static int winner = 0;

	static int row, col;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("Test5.txt"));
		// 여기에 코드를 작성하세요.
		StringTokenizer st;
		for (int i = 0; i < 19; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 19; j++) {
				g[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int j = 0; j < 19; j++) {
			for (int i = 0; i < 19; i++) {
				if (g[i][j] != 0) {
					bfs(i, j);
				}
			}
		}
		System.out.println(winner);
	}

	static void bfs(int x, int y) {
		int stone = g[x][y];
		for (int i = 0; i < 4; i++) {
			int nx = x;
			int ny = y;
			int count = 1;

			int checkX = x + dx1[i];
			int checkY = y + dy1[i];

			if (!(19 <= checkX || checkX < 0 || 19 <= checkY || checkY < 0)) {
				if (g[checkX][checkY] == stone) {
					continue;
				}
			}

			while (true) {
				nx += dx[i];
				ny += dy[i];
				if (19 <= nx || nx < 0 || 19 <= ny || ny < 0) {
					break;
				}
				if (g[nx][ny] == stone) {
					count++;
				} else {
					break;
				}
			}
			if (count == 5) {
				winner = stone;
				row = x + 1;
				col = y + 1;
				System.out.println(winner);
				System.out.println(row + " " + col);
				System.exit(0);
			}
		}
	}
}