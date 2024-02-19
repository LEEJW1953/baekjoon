/**
 * @author 이지원
 * @date 24.02.14
 * @link https://www.acmicpc.net/problem/1074
 * @keyword_solution 
 * 재귀
 * 배열을 4구역으로 나누고, 주어진 좌표가 어느 구역에 있는지 재귀적으로 탐색
 * @input 배열의 크기 N, 좌표 r, c
 * @output r행 c열을 몇 번째로 방문했는지 출력
 * @time_complex 
 * @perf 
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, r, c, N, ans;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		N = (int) Math.pow(2, n);
		z(n, 0, 0);
		System.out.println(ans);
	}

	static void z(int d, int x, int y) {
		if (d == 0) {
			return;
		} else {
			int idx = (int) Math.pow(2, d - 1);
			int tmp = idx * idx;
			int nx = x + idx, ny = y + idx;
			if (r < nx && c < ny) {
				z(d - 1, x, y);
			} else if (r < nx && ny <= c) {
				ans += tmp;
				z(d - 1, x, ny);
			} else if (nx <= r && c < ny) {
				ans += 2 * tmp;
				z(d - 1, nx, y);
			} else {
				ans += 3 * tmp;
				z(d - 1, nx, ny);
			}
		}
	}
}