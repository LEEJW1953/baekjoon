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
		for (int i = 0; i <= n; i++) {
			g[i] = new ArrayList<>();
		}
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (g[a].add(b)) {
				enter[b]++;
			}
		}
		for (int i = 1; i <= n; i++) {
			if (enter[i] == 0) {
				q.add(i);
			}
		}
		while (!q.isEmpty()) {
			int x = q.poll();
			sb.append(x).append(" ");
			for (int i = 0; i < g[x].size(); i++) {
				int next = g[x].get(i);
				enter[next]--;
				if (enter[next] == 0) {
					q.add(next);
				}
			}
		}
		System.out.println(sb);
	}
}