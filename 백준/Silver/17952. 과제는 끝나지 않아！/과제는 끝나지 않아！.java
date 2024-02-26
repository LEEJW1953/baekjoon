import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, total = 0, currScore = 0, currTime = 0;
	static Deque<Task> q = new ArrayDeque<>();

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int type = Integer.parseInt(st.nextToken());
			if (type == 0) {
				if (currScore == 0) {
					continue;
				}
			} else {
				int A = Integer.parseInt(st.nextToken());
				int T = Integer.parseInt(st.nextToken());
				if (currScore > 0) {
					q.offerLast(new Task(currScore, currTime));
				}
				currScore = A;
				currTime = T;
			}
			if (--currTime == 0) {
				total += currScore;
				if (!q.isEmpty()) {
					Task t = q.pollLast();
					currScore = t.score;
					currTime = t.time;
				} else {
					currScore = 0;
					currTime = 0;
				}
			}
		}
		System.out.println(total);
	}
}

class Task {
	int score, time;

	public Task(int a, int t) {
		this.score = a;
		this.time = t;
	}
}