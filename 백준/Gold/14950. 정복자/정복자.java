import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, t, ans = 0, p[];
	static PriorityQueue<Node> pq = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());
		p = new int[n + 1];
		for (int i = 0; i <= n; i++) {
			p[i] = i;
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			pq.offer(new Node(a, b, c));
		}
		int count = 0;
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int a = node.a;
			int b = node.b;
			int c = node.c;
			if (union(a, b)) {
				ans += c + (count * t);
				count++;
			}
		}
		System.out.println(ans);
	}

	static int find(int x) {
		if (x == p[x])
			return x;
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

	static class Node implements Comparable<Node> {
		int a, b, c;

		public Node(int a, int b, int c) {
			this.a = a;
			this.b = b;
			this.c = c;
		}

		@Override
		public int compareTo(Node o) {
			return this.c - o.c;
		}
	}
}