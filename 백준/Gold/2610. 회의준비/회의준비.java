import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, p[], INF = 10000;
	static HashMap<Integer, List<Integer>> map = new HashMap<>();
	static List<Integer>[] g;
	static List<Integer> ans = new ArrayList<>();

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		p = new int[n + 1];
		g = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++) {
			p[i] = i;
			g[i] = new ArrayList<>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			union(a, b);
			g[a].add(b);
			g[b].add(a);
		}
		for (int i = 1; i <= n; i++) {
			p[i] = find(p[i]);
		}
		for (int i = 1; i <= n; i++) {
			if (i == p[i]) {
				map.put(p[i], new ArrayList<>());
			}
			map.get(find(p[i])).add(i);
		}
		sb.append(map.size()).append("\n");
		for (int i : map.keySet()) {
			ans.add(minRoute(map.get(i)));
		}
		Collections.sort(ans, (o1, o2) -> {
			return Integer.compare(o1, o2);
		});
		for (int i : ans) {
			sb.append(i).append("\n");
		}

		System.out.println(sb);
	}

	static int minRoute(List<Integer> list) {
		int total = INF;
		int res = 0;
		int s = list.size();
		int[][] vis = new int[s][s];
		for (int i = 0; i < s; i++) {
			for (int j = 0; j < s; j++) {
				vis[i][j] = INF;
				if (i == j)
					vis[i][j] = 0;
			}
		}
		for (int i = 0; i < s; i++) {
			for (int j : g[list.get(i)]) {
				vis[i][list.indexOf(j)] = 1;
				vis[list.indexOf(j)][i] = 1;
			}
		}
		for (int k = 0; k < s; k++) {
			for (int i = 0; i < s; i++) {
				for (int j = 0; j < s; j++) {
					vis[i][j] = Math.min(vis[i][j], vis[i][k] + vis[k][j]);
				}
			}
		}
		for (int i = 0; i < s; i++) {
			int tmp = 0;
			for (int j = 0; j < s; j++) {
				tmp = Math.max(tmp, vis[i][j]);
			}
			if (tmp < total) {
				res = list.get(i);
				total = tmp;
			}
		}
		return res;
	}

	static int find(int x) {
		if (x == p[x])
			return x;
		return p[x] = find(p[x]);
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