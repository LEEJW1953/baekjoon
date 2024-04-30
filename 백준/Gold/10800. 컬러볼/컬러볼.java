import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, total = 0, prev = 0, count = 1, ans[], color[], colorCount[];
	static PriorityQueue<Ball> pq = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		ans = new int[n];
		color = new int[n + 1];
		colorCount = new int[n + 1];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int c = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			pq.add(new Ball(c, s, i));
		}
		int tmp = 0;
		while (!pq.isEmpty()) {
			Ball ball = pq.poll();
			int s = ball.s, c = ball.c, i = ball.i;
			if (prev < s) {
				prev = s;
				total += tmp * count;
				count = 1;
				colorCount = new int[n + 1];
				tmp = s;
			} else {
				count++;
			}
			ans[i] = total - color[c] + tmp * colorCount[c];
			colorCount[c]++;
			color[c] += tmp;
		}
		for (int i = 0; i < n; i++) {
			sb.append(ans[i]).append("\n");
		}
		System.out.println(sb);
	}

	static class Ball implements Comparable<Ball> {
		int c, s, i;

		public Ball(int c, int s, int i) {
			this.c = c;
			this.s = s;
			this.i = i;
		}

		@Override
		public int compareTo(Ball o) {
			if (this.s == o.s) {
				return this.c - o.c;
			}
			return this.s - o.s;
		}
	}

}