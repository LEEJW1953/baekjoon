import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int l, c;
	static String[] letters, word;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		l = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		letters = new String[c];
		word = new String[l];
		for (int i = 0; i < c; i++) {
			letters[i] = st.nextToken();
		}
		Arrays.sort(letters);
		dfs(0, 0);
		System.out.println(sb);
	}

	static void dfs(int idx, int d) {
		if (d == l) {
			int n1 = 0, n2 = 0;
			for (String c : word) {
				if ("aeiou".contains(c)) {
					n1++;
				} else {
					n2++;
				}
			}
			if (0 < n1 && 1 < n2) {
				sb.append(String.join("", word)).append("\n");
			}
			return;
		}
		for (int i = idx; i < c; i++) {
			word[d] = letters[i];
			dfs(i + 1, d + 1);
		}
	}
}