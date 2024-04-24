import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, k, vis, ans;
	static char[][] word;
	static char[] init = { 'a', 'c', 'i', 'n', 't' };

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		word = new char[n][1];
		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			String tmp = s.substring(4, s.length() - 4);
			word[i] = tmp.toCharArray();
		}
		if (k < 5) {
			System.out.println(0);
			System.exit(0);
		}
		k -= 5;
		for (char c : init) {
			vis |= (1 << (c - 'a'));
		}
		dfs(0, 0);
		System.out.println(ans);
	}

	static void dfs(int d, int idx) {
		if (d == k) {
			ans = Math.max(ans, check());
			return;
		}
		for (int i = idx; i < 26; i++) {
			if ((vis & (1 << i)) == (1 << i))
				continue;
			vis |= (1 << i);
			dfs(d + 1, i);
			vis &= ~(1 << i);
		}
	}

	static int check() {
		int result = 0;
		loop: for (char[] cArr : word) {
			for (char c : cArr) {
				if ((vis & (1 << (c - 'a'))) != (1 << (c - 'a'))) {
					continue loop;
				}
			}
			result++;
		}
		return result;
	}
}