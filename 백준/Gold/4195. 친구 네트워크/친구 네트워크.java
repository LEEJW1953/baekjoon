import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int t, f;
	static HashMap<String, Integer> names;
	static List<int[]> p;

	public static void main(String[] args) throws Exception {
		t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			f = Integer.parseInt(br.readLine());
			names = new HashMap<String, Integer>();
			p = new ArrayList<int[]>();
			int idx = 0;
			for (int j = 0; j < f; j++) {
				st = new StringTokenizer(br.readLine());
				String name1 = st.nextToken();
				String name2 = st.nextToken();
				if (!names.containsKey(name1)) {
					names.put(name1, idx);
					p.add(new int[] { idx++, 1 });
				}
				if (!names.containsKey(name2)) {
					names.put(name2, idx);
					p.add(new int[] { idx++, 1 });
				}
				int a = names.get(name1);
				int b = names.get(name2);
				if (find(a)[0] != find(b)[0]) {
					union(a, b);
				}
				sb.append(find(a)[1]).append("\n");
			}
		}
		System.out.println(sb);
	}

	static int[] find(int x) {
		if (x != p.get(x)[0]) {
			int[] res = find(p.get(x)[0]);
			p.get(x)[0] = res[0];
			p.get(x)[1] = res[1];
		}
		return p.get(x);
	}

	static void union(int x, int y) {
		int[] res1 = find(x);
		int[] res2 = find(y);
		if (res1[0] < res2[0]) {
			p.get(res2[0])[0] = res1[0];
			p.get(res1[0])[1] += res2[1];
		} else {
			p.get(res1[0])[0] = res2[0];
			p.get(res2[0])[1] += res1[1];
		}
	}
}