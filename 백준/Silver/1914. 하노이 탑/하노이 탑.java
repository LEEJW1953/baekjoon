import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static BigInteger count = new BigInteger("2");
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		count = count.pow(n).subtract(new BigInteger("1"));
		sb.append(count).append("\n");

		if (n <= 20) {
			hanoi(n, 1, 3);
		}
		System.out.println(sb);
	}

	static void hanoi(int n, int start, int end) {
		if (n == 1) {
			sb.append(start + " " + end).append("\n");
			return;
		}
		hanoi(n - 1, start, 6 - start - end);
		sb.append(start + " " + end).append("\n");
		hanoi(n - 1, 6 - start - end, end);
	}
}