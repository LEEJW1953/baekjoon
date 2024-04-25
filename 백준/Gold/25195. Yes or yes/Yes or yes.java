import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, s;
	static List<Integer>[] g;
	static boolean[] gom;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<>();
		}
		gom = new boolean[n + 1];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			g[u].add(v);
		}
		s = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < s; i++) {
			int tmp = Integer.parseInt(st.nextToken());
			gom[tmp] = true;
		}
		if (gom[1]) {
			System.out.println("Yes");
			System.exit(0);
		}
		System.out.println(bfs() ? "yes" : "Yes");
	}

	static boolean bfs() {
		Deque<Node> q = new ArrayDeque<>();
		if (g[1].isEmpty()) {
			return true;
		}
		boolean flag = true;
		for (int i = 0; i < g[1].size(); i++) {
			int next = g[1].get(i);
			if (!gom[next]) {
				flag = false;
				q.offer(new Node(1, next));
			}
		}
		if (flag)
			return false;
		while (!q.isEmpty()) {
			Node node = q.poll();
			int prev = node.x;
			int curr = node.y;
			if (gom[curr])
				continue;
			if (g[curr].isEmpty()) {
				return true;
			}
			for (int i = 0; i < g[curr].size(); i++) {
				int next = g[curr].get(i);
				if (!gom[next]) {
					q.offer(new Node(curr, next));
				}
			}
		}
		return false;
	}

	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}