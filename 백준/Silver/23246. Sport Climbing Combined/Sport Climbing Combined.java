import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, b, p, q, r;
	static PriorityQueue<Node> pq = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			b = Integer.parseInt(st.nextToken());
			p = Integer.parseInt(st.nextToken());
			q = Integer.parseInt(st.nextToken());
			r = Integer.parseInt(st.nextToken());
			pq.offer(new Node(b, p, q, r));
		}
		for (int i = 0; i < 3; i++) {
			sb.append(pq.poll().num).append(" ");
		}
		System.out.println(sb);
	}

	static class Node implements Comparable<Node> {
		int num, g, s, b, mul, sum;

		public Node(int num, int g, int s, int b) {
			this.num = num;
			this.g = g;
			this.s = s;
			this.b = b;
			this.mul = g * s * b;
			this.sum = g + s + b;
		}

		@Override
		public int compareTo(Node o) {
			if (this.mul == o.mul) {
				if (this.sum == o.sum) {
					return this.num - o.num;
				}
				return this.sum - o.sum;
			}
			return this.mul - o.mul;
		}
	}
}