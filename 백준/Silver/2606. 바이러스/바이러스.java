import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, M, count, p[];

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		p = new int[N + 1];
		for (int i = 0; i <= N; i++) {
			p[i] = i;
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			union(a, b);
		}
		for (int i = 1; i <= N; i++) {
			if (find(i) == 1) {
				count++;
			}
		}
		System.out.println(count - 1);
	}

	static int find(int x) {
		if (x == p[x]) {
			return x;
		}
		return p[x] = find(p[x]);
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x < y) {
			p[y] = x;
		} else {
			p[x] = y;
		}
	}
}

class Node {
	int a, b;

	public Node(int a, int b) {
		this.a = a;
		this.b = b;
	}
}