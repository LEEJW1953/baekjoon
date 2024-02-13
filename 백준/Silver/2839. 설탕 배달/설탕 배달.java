/**
 * @author 이지원
 * @date 24.02.13
 * @link https://www.acmicpc.net/problem/16435
 * @keyword_solution 그리디 알고리즘
 * 5킬로그램 봉지를 최대한 많이 사용
 * 남은 설탕을 3킬로그램 봉지에 딱 맞게 담을 수 있으면 봉지 개수 출력
 * 그렇지 않으면 5킬로그램 봉지를 하나씩 줄여가며 3킬로그램 봉지에 나눠 담음
 * 5킬로그램 봉지를 사용하지 않아도 3킬로그램 봉지에 나눠담을 수 없는 경우 -1 출력
 * @input 설탕의 무게 N
 * @output 설탕 봉지의 최소 개수, 정확하게 나눌 수 없는 경우 -1 출력
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
	static int N, a, b;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		a = N / 5;
		b = N - 5 * a;
		while (true) {
			if (a == 0 && b % 3 != 0) {
				System.out.println(-1);
				break;
			} else if (b % 3 == 0) {
				System.out.println(a + (b / 3));
				break;
			} else {
				a--;
				b += 5;
			}
		}
	}
}