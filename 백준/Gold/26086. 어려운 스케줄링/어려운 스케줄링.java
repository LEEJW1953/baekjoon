import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, c, k, count = 0, ans;
	static Deque<Integer> qLeft = new ArrayDeque<>();
	static Deque<Integer> qRight = new ArrayDeque<>();
	static boolean order = true;
	static PriorityQueue<Integer> pq = new PriorityQueue<>();
	static PriorityQueue<Integer> pq2 = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		for (int i = 0; i < c; i++) {
			st = new StringTokenizer(br.readLine());
			int com = Integer.parseInt(st.nextToken());
			int num = 0;
			if (com == 0) {
				num = Integer.parseInt(st.nextToken());
				if (order) {
					qLeft.offerFirst(num);
				} else {
					qRight.offerLast(num);
				}
			} else if (com == 1) {
				order = true;
				while (!qLeft.isEmpty()) {
					int tmp = qLeft.poll();
					pq.offer(tmp);
					pq2.offer(-1 * tmp);
				}
				while (!qRight.isEmpty()) {
					int tmp = qRight.poll();
					pq.offer(tmp);
					pq2.offer(-1 * tmp);
				}
			} else {
				order = !order;
			}
		}
		if (order) {
			while (count < k && !qLeft.isEmpty()) {
				int num;
				num = qLeft.pollFirst();
				ans = num;
				count++;
			}
			while (count < k && !pq.isEmpty()) {
				int num;
				num = pq.poll();
				ans = num;
				count++;
			}
			while (count < k && !qRight.isEmpty()) {
				int num;
				num = qRight.pollFirst();
				ans = num;
				count++;
			}
		} else {
			while (count < k && !qRight.isEmpty()) {
				int num;
				num = qRight.pollLast();
				ans = num;
				count++;
			}
			while (count < k && !pq2.isEmpty()) {
				int num;
				num = pq2.poll() * -1;
				ans = num;
				count++;
			}
			while (count < k && !qLeft.isEmpty()) {
				int num;
				num = qLeft.pollLast();
				ans = num;
				count++;
			}
		}
		System.out.println(ans);
	}
}