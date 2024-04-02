import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int P = 15 * 100000;

	public static void main(String[] args) throws Exception {
		long n = Long.parseLong(br.readLine());
		int m = (int) (n % P);
		int[] fib = new int[m + 1];
		fib[0] = 0;
		fib[1] = 1;
		for (int i = 2; i <= m; i++) {
			fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000;
		}
		System.out.println(fib[m]);
	}
}