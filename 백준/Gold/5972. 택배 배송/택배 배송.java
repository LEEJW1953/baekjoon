import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m;
	static List<Node>[] g;
	static int INF = Integer.MAX_VALUE;
	static int[] dis;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<>();
		}
		dis = new int[n + 1];
		Arrays.fill(dis, INF);
		dis[1] = 0;
		for (int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			g[a].add(new Node(b, c));
			g[b].add(new Node(a, c));
		}
		dijk(1);
		System.out.println(dis[n]);
	}

	public static void dijk(int start) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		while (!pq.isEmpty()) {
			Node curr = pq.poll();
			int n = curr.n;
			int d = curr.d;
			for (Node node : g[n]) {
				int cost = node.d + d;
				if (cost < dis[node.n]) {
					dis[node.n] = cost;
					pq.add(new Node(node.n, cost));
				}
			}
		}
	}
}

class Node implements Comparable<Node> {
	int n;
	int d;

	public Node(int n, int d) {
		this.n = n;
		this.d = d;
	}

	@Override
	public int compareTo(Node o) {
		// TODO Auto-generated method stub
		return this.d - o.d;
	}
}