import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, enter[];
	static List<Integer>[] g;
	static Deque<Integer> q = new ArrayDeque<Integer>();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		enter = new int[n + 1];
		g = new ArrayList[n + 1];
		boolean[] vis = new boolean[n + 1];
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			g[a].add(b);
			enter[b]++;
		}
		for (int i = 1; i <= n; i++) {
			if (enter[i] == 0) {
				q.add(i);
			}
		}
		while (!q.isEmpty()) {
			int node = q.poll();
			vis[node] = true;
			sb.append(node).append(" ");
			for (int i = 0; i < g[node].size(); i++) {
				int next = g[node].get(i);
				enter[next]--;
				if (enter[next] == 0) {
					q.add(next);
				}
			}
		}
		System.out.println(sb);
	}
}