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
	static int N, M;
	static List<Node>[] g;
	static long INF = 2000000000000L;
	static long[] dis;
	static int[] valid;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		g = new ArrayList[N + 1];
		dis = new long[N + 1];
		dis[0] = 0;
		valid = new int[N + 1];
		for (int i = 0; i <= N; i++) {
			g[i] = new ArrayList<>();
		}
		Arrays.fill(dis, INF);

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			valid[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			g[a].add(new Node(b, c));
			g[b].add(new Node(a, c));
		}
		dijk(0);
		System.out.println(dis[N - 1] == INF ? -1 : dis[N - 1]);
	}

	public static void dijk(int start) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		while (!pq.isEmpty()) {
			Node curr = pq.poll();
			int n = curr.n;
			long d = curr.d;

			if (dis[n] < d) {
				continue;
			}

			for (Node node : g[n]) {
				long cost = node.d + d;
				if (cost < dis[node.n]) {
					if (valid[node.n] == 0) {
						dis[node.n] = cost;
						pq.add(new Node(node.n, cost));
					} else if (node.n == N - 1) {
						dis[node.n] = cost;
						pq.add(new Node(node.n, cost));
					}
				}
			}
		}
	}
}

class Node implements Comparable<Node> {
	int n;
	long d;

	public Node(int n, long d) {
		this.n = n;
		this.d = d;
	}

	@Override
	public int compareTo(Node o) {
		long res = this.d - o.d;
		if (res != 0) {
			return (int) (res / Math.abs(res));
		}
		return 0;
	}
}