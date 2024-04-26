import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st, st2;
	static StringBuilder sb = new StringBuilder();
	static int n, ans, count[];

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		count = new int[n];
		st = new StringTokenizer(br.readLine());
		st2 = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			count[i] = Integer.parseInt(st.nextToken()) - Integer.parseInt(st2.nextToken());
		}
		while (true) {
			if (check()) {
				break;
			}
			for (int i = 0; i < n; i++) {
				if (count[i] == 0)
					continue;
				boolean flag = count[i] > 0;
				int[] result = solve(i, flag);
				for (int j = i; j <= result[1]; j++) {
					count[j] -= result[0];
				}
				ans += Math.abs(result[0]);
				break;
			}
		}
		System.out.println(ans);
	}

	static int[] solve(int start, boolean flag) {
		int val = flag ? Integer.MAX_VALUE : Integer.MIN_VALUE;
		int end = start;
		if (flag) {
			for (int i = start; i < n; i++) {
				if (count[i] > 0 != flag || count[i] == 0) {
					break;
				}
				val = Math.min(val, (count[i]));
				end = i;
			}
		} else {
			for (int i = start; i < n; i++) {
				if (count[i] > 0 != flag || count[i] == 0) {
					break;
				}
				val = Math.max(val, count[i]);
				end = i;
			}
		}
		return new int[] { val, end };
	}

	static boolean check() {
		for (int i = 0; i < n; i++) {
			if (count[i] != 0) {
				return false;
			}
		}
		return true;
	}
}