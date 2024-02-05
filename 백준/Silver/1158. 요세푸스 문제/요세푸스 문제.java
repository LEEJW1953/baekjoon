import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, k;
	static Deque<Integer> q = new ArrayDeque<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= n; i++) {
			q.offer(i);
		}
		sb.append("<");
		while (!q.isEmpty()) {
			for (int i = 0; i < k - 1; i++) {
				q.offerLast(q.pollFirst());
			}
			if (q.size() != 1) {
				sb.append(q.pollFirst()).append(", ");
			} else {
				sb.append(q.pollFirst());
			}
		}
		sb.append(">");
		System.out.println(sb);
	}
}