import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n;
	static int[] tower;
	static Deque<int[]> stack = new ArrayDeque<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		tower = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			tower[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0; i < n; i++) {
			if (stack.isEmpty()) {
				stack.offer(new int[] { tower[i], i + 1 });
				sb.append("0 ");
			} else {
				int h = tower[i];
				while (!stack.isEmpty() && stack.peekLast()[0] < h) {
					stack.pollLast();
				}
				if (stack.isEmpty()) {
					sb.append("0 ");
				} else {
					sb.append(stack.peekLast()[1] + " ");
				}
				stack.offerLast(new int[] { h, i + 1 });
			}
		}
		System.out.println(sb);
	}

}