import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, v;
	static List<Integer>[] g;
	static boolean[] vis;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());
		g = new ArrayList[n + 1];
		vis = new boolean[n + 1];
		for (int i = 1; i <= n; i++) {
			g[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			g[a].add(b);
			g[b].add(a);
		}
		for (int i = 1; i <= n; i++) {
			Collections.sort(g[i]);
		}
		dfs(v);
		sb.append("\n");
		bfs();
		System.out.println(sb);
	}

	static void bfs() {
		boolean[] vis = new boolean[n + 1];
		Deque<Integer> q = new ArrayDeque<Integer>();
		q.offer(v);
		vis[v] = true;
		sb.append(v + " ");
		while (!q.isEmpty()) {
			int node = q.poll();
			for (int n : g[node]) {
				if (!vis[n]) {
					q.offer(n);
					vis[n] = true;
					sb.append(n + " ");
				}
			}
		}
	}

	static void dfs(int node) {
		vis[node] = true;
		sb.append(node + " ");
		for (int n : g[node]) {
			if (!vis[n]) {
				dfs(n);
			}
		}
	}
}