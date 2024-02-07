/**
 * @author 이지원
 * @date 2024.02.07
 * @link https://www.acmicpc.net/problem/11286
 * @keyword_solution 절댓값이 작은 값을 기준으로, 절댓값이 같으면 작은 값을 기준으로 정렬 
 * @input 
 * @output 
 * @time_complex 
 * @perf 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n;
	static Queue<Node> pq = new PriorityQueue<>();

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			if (x == 0) {
				if (pq.isEmpty()) {
					sb.append(0).append("\n");
				} else {
					sb.append(pq.poll().x).append("\n");
				}
			} else {
				pq.offer(new Node(x));
			}
		}
		System.out.println(sb);
	}
}

class Node implements Comparable<Node> {
	int x;
	int absX;

	public Node(int x) {
		this.x = x;
		this.absX = Math.abs(x);
	}

	@Override
	public int compareTo(Node o) {
		if (Integer.compare(this.absX, o.absX) == 0) {
			return Integer.compare(this.x, o.x);
		}
		return Integer.compare(this.absX, o.absX);
	}
}