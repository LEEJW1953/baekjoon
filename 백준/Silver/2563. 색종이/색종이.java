/**
 * @author 이지원
 * @date 2024.02.07
 * @link https://www.acmicpc.net/problem/2563
 * @keyword_solution 10*10 크기의 색종이가 붙은 영역을 모두 저장
 * @input 
 * 색종이의 개수 N
 * N개의 줄에 걸쳐 색종이의 위치 입력
 * @output 
 * 색종이가 붙어있는 영역의 넓이 출력
 * @time_complex 
 * @perf 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int INF = Integer.MAX_VALUE;
	static int n;
	static int[][] g = new int[100][100];
	static int ans = 0;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			for (int j = x; j < x + 10; j++) {
				for (int k = y; k < y + 10; k++) {
					g[j][k] = 1;
				}
			}
		}
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (g[i][j] == 1) {
					ans++;
				}
			}
		}
		System.out.println(ans);
	}
}