import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, p[], ans = 0;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		p = new int[n];
		for (int i = 0; i < n; i++) {
			p[i] = i;
		}
		for (int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			if (find(x) == find(y) && ans == 0) {
				ans = i;
			} else {
				union(x, y);
			}
		}
		System.out.println(ans);
	}

	static int find(int x) {
		if (x != p[x]) {
			p[x] = find(p[x]);
		}
		return p[x];
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