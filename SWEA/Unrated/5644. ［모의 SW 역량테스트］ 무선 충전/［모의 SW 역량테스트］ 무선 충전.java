/**
 * @author 이지원
 * @date 24.02.15
 * @link https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY0LFFoqrIIDFAXz&contestProbId=AWXRDL1aeugDFAUo&probBoxId=AY2gBgM6OSIDFAXh&type=PROBLEM&problemBoxTitle=0212%EC%A3%BC&problemBoxCnt=5
 * @keyword_solution 
 * @input 
 * @output 
 * @time_complex
 * @perf
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int tc, M, A, X, Y, C, P;
	static int moveA[], moveB[], charger[];
	static int[][] d = { { 0, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 }, { -1, 0 } };
	static int xa = 1, ya = 1, xb = 10, yb = 10, ans = 0;
	static List<Integer>[][] G = new ArrayList[11][11];

	public static void main(String[] args) throws IOException {
		tc = Integer.parseInt(br.readLine());
		for (int t = 1; t <= tc; t++) {
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			moveA = new int[M + 1];
			moveB = new int[M + 1];
			charger = new int[A + 1];
			G = new ArrayList[11][11];
			xa = 1;
			ya = 1;
			xb = 10;
			yb = 10;
			ans = 0;

			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= M; i++) {
				moveA[i] = Integer.parseInt(st.nextToken());
			}

			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= M; i++) {
				moveB[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 1; i <= A; i++) {
				st = new StringTokenizer(br.readLine());
				X = Integer.parseInt(st.nextToken());
				Y = Integer.parseInt(st.nextToken());
				C = Integer.parseInt(st.nextToken());
				P = Integer.parseInt(st.nextToken());
				charger[i] = P;
				place(X, Y, C, i);
			}

			for (int i = 0; i <= M; i++) {
				charge(i);
			}
			sb.append("#" + t + " " + ans).append("\n");
		}
		System.out.println(sb);
	}

	static void place(int x, int y, int c, int n) {
		for (int i = 1; i <= 10; i++) {
			for (int j = 1; j <= 10; j++) {
				if ((Math.abs(x - i) + Math.abs(y - j)) <= c) {
					if (G[i][j] == null) {
						G[i][j] = new ArrayList<Integer>();
					}
					G[i][j].add(n);
				}
			}
		}
	}

	static void charge(int m) {
		xa += d[moveA[m]][0];
		ya += d[moveA[m]][1];
		xb += d[moveB[m]][0];
		yb += d[moveB[m]][1];
		List<Integer> chargeA = G[xa][ya];
		List<Integer> chargeB = G[xb][yb];
		int amount = 0;
//		System.out.println(m + " : " + chargeA + " " + chargeB);
		if (chargeA == null & chargeB == null) {
			return;
		} else if (chargeB == null) {
			for (int c : chargeA) {
				amount = Math.max(amount, charger[c]);
			}
			ans += amount;
		} else if (chargeA == null) {
			for (int c : chargeB) {
				amount = Math.max(amount, charger[c]);
			}
			ans += amount;
		} else {
			for (int c1 : chargeA) {
				for (int c2 : chargeB) {
					int sum;
					if (c1 == c2) {
						sum = charger[c1];
					} else {
						sum = charger[c1] + charger[c2];
					}
					amount = Math.max(amount, sum);
				}
			}
			ans += amount;
		}
		return;
	}
}