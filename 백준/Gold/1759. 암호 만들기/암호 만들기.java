import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int L, C;
	static List<String> letters = new ArrayList<>();
	static List<String> word = new ArrayList<>();
	static List<String> answer = new ArrayList<>();
	static List<String> vowel = new ArrayList<>(Arrays.asList("a", "e", "i", "o", "u"));

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < C; i++) {
			letters.add(st.nextToken());
		}
		Collections.sort(letters);
		combination(0, 0);
		System.out.println(sb);
	}

	static void combination(int d, int idx) {
		if (d == L) {
			int n1 = 0;
			int n2 = 0;
			for (String s : word) {
				if (vowel.contains(s)) {
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
		for (int i = idx; i < C; i++) {
			word.add(letters.get(i));
			combination(d + 1, i + 1);
			word.remove(word.size() - 1);
		}
	}
}