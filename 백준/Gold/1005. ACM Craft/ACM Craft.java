import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, K, D[], enter[], ans, vis[], W;
	static List<Integer>[] g;
	static Queue<Integer> q;

	public static void main(String[] args) throws Exception {
		T = Integer.parseInt(br.readLine());
		test: for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			ans = 0;
			D = new int[N + 1];
			enter = new int[N + 1];
			g = new ArrayList[N + 1];
			vis = new int[N + 1];
			q = new ArrayDeque<>();
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= N; i++) {
				D[i] = Integer.parseInt(st.nextToken());
				g[i] = new ArrayList<>();
			}
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				enter[y]++;
				g[x].add(y);
			}
			W = Integer.parseInt(br.readLine());
			for (int i = 1; i <= N; i++) {
				if (enter[i] == 0) {
					q.offer(i);
					vis[i] = D[i];
					if (i == W) {
						sb.append(vis[W]).append("\n");
						continue test;
					}
				}
			}
			while (!q.isEmpty()) {
				int w = q.poll();
				for (int i = 0; i < g[w].size(); i++) {
					int next = g[w].get(i);
					enter[next]--;
					vis[next] = Math.max(vis[next], vis[w] + D[next]);
					if (enter[next] == 0) {
						q.offer(next);
						if (next == W) {
							sb.append(vis[W]).append("\n");
							continue test;
						}
					}
				}
			}
		}
		System.out.println(sb);
	}
}