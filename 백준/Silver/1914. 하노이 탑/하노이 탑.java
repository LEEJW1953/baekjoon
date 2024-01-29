import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static BigInteger count = new BigInteger("2");

	public static void main(String[] args) throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		count = count.pow(n).subtract(new BigInteger("1"));
		System.out.println(count);

		if (n <= 20) {
			hanoi(n, 1, 3);
		}
	}

	static void hanoi(int n, int start, int end) {
		if (n == 1) {
			System.out.println(start + " " + end);
			return;
		}
		hanoi(n - 1, start, 6 - start - end);
		System.out.println(start + " " + end);
		hanoi(n - 1, 6 - start - end, end);
	}
}