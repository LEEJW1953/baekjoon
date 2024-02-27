import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int V, E, p[], count = 0, ans = 0;
	static PriorityQueue<Node> pq = new PriorityQueue<Node>();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		p = new int[V + 1];
		for (int i = 0; i <= V; i++) {
			p[i] = i;
		}
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			pq.offer(new Node(a, b, c));
		}
		while (count < V - 1 && !pq.isEmpty()) {
			Node n = pq.poll();
			if (union(n.from, n.to)) {
				count++;
				ans += n.dist;
			}
		}
		System.out.println(ans);
	}

	static int find(int x) {
		if (x == p[x]) {
			return x;
		}
		return p[x] = find(p[x]);
	}

	static boolean union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y)
			return false;
		if (x < y) {
			p[y] = x;
		} else {
			p[x] = y;
		}
		return true;
	}
}

class Node implements Comparable<Node> {
	int from, to, dist;

	public Node(int a, int b, int c) {
		this.from = a;
		this.to = b;
		this.dist = c;
	}

	public int compareTo(Node o) {
		return this.dist - o.dist;
	}
}