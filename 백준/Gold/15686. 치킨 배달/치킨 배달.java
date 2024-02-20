import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int[][] g;
	static List<Coord> chicken = new ArrayList<Coord>();
	static List<Coord> home = new ArrayList<Coord>();
	static boolean[] selected;
	static int ans = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int nextInt = Integer.parseInt(st.nextToken());
				if (nextInt == 1) {
					home.add(new Coord(i, j));
				} else if (nextInt == 2) {
					chicken.add(new Coord(i, j));
				}
			}
		}
		selected = new boolean[chicken.size()];

		select(0, 0);
		System.out.println(ans);
	}

	static void select(int d, int idx) {
		if (d == m) {
			int total = 0;
			for (Coord h : home) {
				int tmp = Integer.MAX_VALUE;
				for (int i = 0; i < chicken.size(); i++) {
					if (!selected[i]) {
						continue;
					}
					Coord chk = chicken.get(i);
					tmp = Math.min(tmp, h.compareTo(chk));
				}
				total += tmp;
				if (total > ans) {
					return;
				}
			}
			ans = Math.min(ans, total);
			return;
		}
		for (int i = idx; i < chicken.size(); i++) {
			selected[i] = true;
			select(d + 1, i + 1);
			selected[i] = false;
		}
	}
}

class Coord implements Comparable<Coord> {
	int x;
	int y;

	public Coord(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int compareTo(Coord o) {
		return Math.abs(this.x - o.x) + Math.abs(this.y - o.y);
	}
}