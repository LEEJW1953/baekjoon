import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int P = 15 * 100_000_000, n, a, b, MOD = 1_000_000_000;
	static HashMap<Integer, Long> F = new HashMap<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		a = (int) ((Long.parseLong(st.nextToken()) + 1) % P);
		b = (int) ((Long.parseLong(st.nextToken()) + 2) % P);
		F.put(0, 0L);
		F.put(1, 1L);
		F.put(2, 1L);
		System.out.println((fibo(b) - fibo(a) + MOD) % MOD);
	}

	static Long fibo(int x) {
		if (F.containsKey(x)) {
			return F.get(x);
		}
		if (x % 2 == 0) {
			Long f1 = fibo(x / 2) % MOD;
			Long f2 = fibo(x / 2 - 1) % MOD;
			F.put(x / 2, f1);
			F.put(x / 2 - 1, f2);
			return (f1 * (((2 * f2) % MOD + f1) % MOD)) % MOD;
		} else {
			Long f1 = fibo(x / 2) % MOD;
			Long f2 = fibo(x / 2 + 1) % MOD;
			F.put(x / 2, f1);
			F.put(x / 2 + 1, f2);
			return ((f1 * f1) % MOD + (f2 * f2) % MOD) % MOD;
		}
	}
}