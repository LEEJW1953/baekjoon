import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, startX, startY, endX, endY;
	static boolean[][] dp;
	static List<Node> list;

	public static void main(String[] args) throws Exception {
		T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			N = Integer.parseInt(br.readLine());
			dp = new boolean[N + 2][N + 2];
			list = new ArrayList<>();
			for (int i = 0; i < N + 2; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				list.add(new Node(x, y));
			}
			for (int i = 0; i < N + 2; i++) {
				for (int j = 0; j < N + 2; j++) {
					if (i == j) {
						dp[i][j] = false;
					} else {
						dp[i][j] = list.get(i).compareTo(list.get(j)) > 0;
					}
				}
			}
			for (int k = 0; k < N + 2; k++) {
				for (int i = 0; i < N + 2; i++) {
					for (int j = 0; j < N + 2; j++) {
						if (!dp[i][j]) {
							dp[i][j] = dp[i][k] && dp[k][j];
						}
					}
				}
			}
			if (dp[0][N + 1]) {
				sb.append("happy").append("\n");
			} else {
				sb.append("sad").append("\n");
			}
		}
		System.out.println(sb);
	}

	static class Node implements Comparable<Node> {
		int x;
		int y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public int compareTo(Node o) {
			int dist = Math.abs(this.x - o.x) + Math.abs(this.y - o.y);
			return dist <= 1000 ? 1 : -1;
		}
	}
}