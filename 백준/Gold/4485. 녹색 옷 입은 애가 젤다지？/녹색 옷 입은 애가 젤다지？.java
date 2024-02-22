import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, g[][];
	static int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws Exception {
		int idx = 0;
		while (true) {
			idx++;
			n = Integer.parseInt(br.readLine());
			if (n == 0) {
				break;
			}
			g = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					g[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			sb.append("Problem " + idx + ": " + dijkstra()).append("\n");
		}
		System.out.println(sb);
	}

	static int dijkstra() {
		int[][] vis = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				vis[i][j] = -1;
			}
		}
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		pq.add(new Node(new int[] { 0, 0 }, g[0][0]));
		vis[0][0] = g[0][0];
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int xx = node.to[0], yy = node.to[1], dd = node.dist;
			for (int i = 0; i < 4; i++) {
				int nx = xx + dx[i], ny = yy + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					int cost = dd + g[nx][ny];
					if (vis[nx][ny] == -1 || cost < vis[nx][ny]) {
						pq.add(new Node(new int[] { nx, ny }, cost));
						vis[nx][ny] = cost;
					}
				}
			}
		}
		return vis[n - 1][n - 1];
	}
}

class Node implements Comparable<Node> {
	int[] to;
	int dist;

	public Node(int[] n, int d) {
		this.to = n;
		this.dist = d;
	}

	public int compareTo(Node o) {
		return Integer.compare(this.dist, o.dist);
	}
}