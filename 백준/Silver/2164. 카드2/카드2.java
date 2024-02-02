/**
 * @author 이지원
 * @date 2024.02.02
 * @link https://www.acmicpc.net/problem/2164
 * @keyword_solution 
 * 큐에서 맨 앞의 숫자를 하나 제거한다
 * 그 다음 맨 앞의 숫자를 맨 뒤에 추가한다
 * 큐에 하나의 숫자가 남을 때 까지 반복하고, 마지막 남은 숫자를 출력한다
 * @input 1<=N<=500000 인 정수 1개
 * @output 마지막 남은 숫자 1개
 * @time_complex O(N)
 * @perf 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static Queue<Integer> q = new LinkedList<>();

	public static void main(String[] args) throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= n; i++) {
			q.add(i);
		}
		while (q.size() > 1) {
			q.poll();
			q.add(q.poll());
		}
		System.out.println(q.poll());
	}
}