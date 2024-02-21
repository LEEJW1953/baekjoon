import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int tc, n, m;
	static List<Integer>[] g;
	static boolean[] vis;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new ArrayList[n];
		vis = new boolean[n];
		for (int i = 0; i < n; i++) {
			g[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			g[a].add(b);
			g[b].add(a);
		}
		for (int i = 0; i < n; i++) {
			vis[i] = true;
			if (dfs(i, 0)) {
				System.out.println(1);
				System.exit(0);
			}
			vis[i] = false;
		}
		System.out.println(0);
	}

	static boolean dfs(int idx, int d) {
		if (d == 4) {
			return true;
		}
		for (int i : g[idx]) {
			if (!vis[i]) {
				vis[i] = true;
				if (dfs(i, d + 1)) {
					return true;
				}
				vis[i] = false;
			}
		}
		return false;
	}
}