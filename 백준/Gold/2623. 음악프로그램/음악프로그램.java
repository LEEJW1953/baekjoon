import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, m, enter[];
	static List<Integer>[] g;
	static PriorityQueue<Integer> q = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new ArrayList[n + 1];
		enter = new int[n + 1];
		boolean[] vis = new boolean[n + 1];
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int a = 0, b = 0;
			a = Integer.parseInt(st.nextToken());
			for (int j = 0; j < t - 1; j++) {
				b = Integer.parseInt(st.nextToken());
				g[a].add(b);
				enter[b]++;
				a = b;
			}
		}
		for (int i = 1; i <= n; i++) {
			if (enter[i] == 0) {
				q.add(i);
			}
		}
		while (!q.isEmpty()) {
			int x = q.poll();
			vis[x] = true;
			sb.append(x).append("\n");
			for (int i = 0; i < g[x].size(); i++) {
				int next = g[x].get(i);
				enter[next]--;
				if (enter[next] == 0) {
					q.add(next);
				}
			}
		}
		for (int i = 1; i <= n; i++) {
			if (!vis[i]) {
				System.out.println(0);
				System.exit(0);
			}
		}
		System.out.println(sb);
	}
}