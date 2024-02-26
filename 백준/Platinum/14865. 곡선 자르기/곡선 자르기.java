import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, startX, startY, prevX = 0, prevY = 0, count1 = 0, count2 = 0;
	static PriorityQueue<Coord> h = new PriorityQueue<Coord>();
	static Deque<Integer> stack = new ArrayDeque<Integer>();

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			if (i == 0) {
				startX = x;
				startY = y;
			}
			if ((prevY * y) < 0) {
				h.add(new Coord(x, Math.max(prevY, y)));
			}
			prevX = x;
			prevY = y;
		}
		if (prevY * startY < 0) {
			h.add(new Coord(prevX, Math.max(prevY, startY)));
		}
		while (!h.isEmpty()) {
			Coord c = h.poll();
			int y = c.y;
			if (stack.isEmpty()) {
				stack.offerLast(y);
				if (!h.isEmpty() && h.peek().y == y) {
					count2++;
				}
			} else {
				if (stack.peekLast() == y) {
					stack.pollLast();
					if (stack.isEmpty()) {
						count1++;
					}
				} else {
					stack.offerLast(y);
					if (h.peek().y == y) {
						count2++;
					}
				}
			}
		}
		System.out.println(count1 + " " + count2);
	}
}

class Coord implements Comparable<Coord> {
	int x, y;

	public Coord(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int compareTo(Coord o) {
		return Integer.compare(this.x, o.x);
	}
}