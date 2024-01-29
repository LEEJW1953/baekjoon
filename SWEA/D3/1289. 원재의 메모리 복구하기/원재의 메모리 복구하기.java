import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int t;

	public static void main(String[] args) throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		t = Integer.parseInt(st.nextToken());
		for (int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			String s = st.nextToken();
			char prev = '0';
			int count = 0;
			for (int j = 0; j < s.length(); j++) {
				if (s.charAt(j) != prev) {
					prev = s.charAt(j);
					count++;
				}
			}
			System.out.println("#" + (i + 1) + " " + count);
		}
	}
}