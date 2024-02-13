import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, p[];
	static char[][] g;
	static HashSet<Integer> set = new HashSet<Integer>();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		p = new int[n * m];
		g = new char[n][m];
		for (int i = 0; i < p.length; i++) {
			p[i] = i;
		}
		for (int i = 0; i < n; i++) {
			g[i] = br.readLine().toCharArray();
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int curr = i * m + j;
				int next = nextIdx(i, j);
				if (find(curr) != find(next)) {
					union(curr, next);
				}
			}
		}

		for (int i = 0; i < p.length; i++) {
			set.add(find(i));
		}
		System.out.println(set.size());
	}

	static int nextIdx(int x, int y) {
		switch (g[x][y]) {
		case 'U':
			x--;
			break;
		case 'D':
			x++;
			break;
		case 'L':
			y--;
			break;
		case 'R':
			y++;
			break;
		}
		return x * m + y;
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