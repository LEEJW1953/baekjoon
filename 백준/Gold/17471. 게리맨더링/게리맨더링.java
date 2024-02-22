import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int n, city[], total, ans = Integer.MAX_VALUE;
	static List<Integer>[] g;
	static boolean[] side, vis;

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		city = new int[n];
		g = new ArrayList[n];
		side = new boolean[n];
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(st.nextToken());
			city[i] = num;
			total += num;
			g[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			for (int j = 0; j < m; j++) {
				int c = Integer.parseInt(st.nextToken());
				g[i].add(c - 1);
			}
		}
		split();
		System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);
	}

	static void split() {
		for (int i = 1; i < (1 << n) - 1; i++) {
			int sum = 0;
			for (int j = 0; j < n; j++) {
				boolean tmp = (i & 1 << j) != 0;
				side[j] = tmp;
				if (tmp) {
					sum += city[j];
				}
			}
			solve(sum);
		}
	}

	static void solve(int sum) {
		int res = Math.abs(total - 2 * sum);
		if (ans < res) {
			return;
		}
		vis = new boolean[n];
		int count = 0;
		for (int i = 0; i < n; i++) {
			if (!vis[i]) {
				dfs(i, side[i]);
				count++;
			}
		}
		if (count != 2) {
			return;
		}
		for (int i = 0; i < n; i++) {
			if (!vis[i]) {
				return;
			}
		}
		ans = Math.min(ans, res);
	}

	static void dfs(int idx, boolean bool) {
		vis[idx] = true;
		for (int i : g[idx]) {
			if (!vis[i] && (side[i] == bool)) {
				dfs(i, bool);
			}
		}
	}
}