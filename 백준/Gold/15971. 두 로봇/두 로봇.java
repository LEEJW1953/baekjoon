import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, r1, r2, INF = Integer.MAX_VALUE;
	static List<Node>[] g;
	static int[][] vis;
	static PriorityQueue<Node> pq = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r1 = Integer.parseInt(st.nextToken());
		r2 = Integer.parseInt(st.nextToken());
		g = new List[n + 1];
		vis = new int[n + 1][2];
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<>();
			vis[i][0] = INF;
			vis[i][1] = 0;
		}
		for (int i = 0; i < n - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			g[a].add(new Node(a, b, c));
			g[b].add(new Node(b, a, c));
		}
		dijkstra();
		System.out.println(vis[r2][0] - vis[r2][1]);
	}

	static void dijkstra() {
		vis[r1][0] = 0;
		for (int i = 0; i < g[r1].size(); i++) {
			Node node = g[r1].get(i);
			pq.offer(node);
			vis[node.y][0] = node.c;
			vis[node.y][1] = node.c;
		}
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int y = node.y;
			int c = node.c;
			for (int i = 0; i < g[y].size(); i++) {
				Node next = g[y].get(i);
				int cost = c + next.c;
				if (vis[next.y][0] < cost)
					continue;
				pq.offer(new Node(next.x, next.y, cost));
				vis[next.y][0] = cost;
				vis[next.y][1] = Math.max(vis[next.x][1], next.c);
			}
		}
	}

	static class Node implements Comparable<Node> {
		int x, y, c;

		public Node(int x, int y, int c) {
			this.x = x;
			this.y = y;
			this.c = c;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.c, o.c);
		}
	}
}