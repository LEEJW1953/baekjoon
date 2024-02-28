import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int t, n;
	static BigInteger ans;

	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			st = new StringTokenizer(br.readLine());
			ans = new BigInteger("1");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			for (int j = 0; j < a; j++) {
				ans = ans.multiply(new BigInteger((b - j) + ""));
			}
			for (int j = 1; j <= a; j++) {
				ans = ans.divide(new BigInteger(j + ""));
			}
			sb.append(ans).append("\n");
		}
		System.out.println(sb);
	}
}