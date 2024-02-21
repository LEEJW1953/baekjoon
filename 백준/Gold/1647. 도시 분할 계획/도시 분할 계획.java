import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, m, total = 0, maxx = 0, count = 0;
	static int[] p;
	static PriorityQueue<Edge> pq = new PriorityQueue<Edge>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		p = new int[n + 1];
		for (int i = 0; i <= n; i++) {
			p[i] = i;
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			pq.offer(new Edge(a, b, c));
		}

		while (!pq.isEmpty() || count < n - 1) {
			Edge e = pq.poll();
			int a = e.from;
			int b = e.to;
			int d = e.dist;
			if (find(a) != find(b)) {
				count++;
				union(a, b);
				total += d;
				maxx = d;
			}
		}
		System.out.println(total - maxx);
	}

	static int find(int x) {
		if (x != p[x]) {
			p[x] = find(p[x]);
		}
		return p[x];
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x < y) {
			p[y] = x;
		} else {
			p[x] = y;
		}
	}
}

class Edge implements Comparable<Edge> {
	int from;
	int to;
	int dist;

	public Edge(int a, int b, int d) {
		this.from = a;
		this.to = b;
		this.dist = d;
	}

	public int compareTo(Edge o) {
		return Integer.compare(this.dist, o.dist);
	}
}