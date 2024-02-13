/**
 * @author 이지원
 * @date 24.02.13
 * @link https://www.acmicpc.net/problem/16435
 * @keyword_solution 과일의 높이 정렬 후 스네이크버드의 현재 길이보다 작을 경우 스네이크버드의 길이 증가
 * @input 
 * 과일의 개수 N, 초기 길이 L
 * 과일의 높이 h1, h2, ... hN
 * @output 스네이크버드의 최대 길이
 * @time_complex 
 * @perf 
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, L, h[];

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		h = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			h[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(h);
		for (int i : h) {
			if (i <= L) {
				L++;
			}
		}
		System.out.println(L);
	}
}