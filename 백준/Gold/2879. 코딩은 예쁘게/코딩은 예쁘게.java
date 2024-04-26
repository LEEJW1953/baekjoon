import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, ans, ind[], res[], count[];

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		ind = new int[n];
		res = new int[n];
		count = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			ind[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			res[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0; i < n; i++) {
			count[i] = res[i] - ind[i];
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
				if (flag) {
					for (int j = i; j <= result[1]; j++) {
						count[j] -= result[0];
					}
				} else {
					for (int j = i; j <= result[1]; j++) {
						count[j] += result[0];
					}
				}
				ans += result[0];
				break;
			}
		}
		System.out.println(ans);
	}

	static int[] solve(int start, boolean flag) {
		int val = Integer.MAX_VALUE;
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
				val = Math.min(val, (count[i] * -1));
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