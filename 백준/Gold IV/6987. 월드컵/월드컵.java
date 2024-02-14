/**
 * @author 이지원
 * @date 24.02.14
 * @link https://www.acmicpc.net/problem/6987
 * @keyword_solution 
 * @input 
 * @output 
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
	static int g[][] = new int[6][3], ans, tmp[][];
	static boolean[][] vis;
	static int[] home = { 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4 };
	static int[] away = { 1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5 };

	public static void main(String[] args) throws IOException {
		loop: for (int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			ans = 0;
			int total = 0;
			for (int j = 0; j < 6; j++) {
				for (int k = 0; k < 3; k++) {
					int num = Integer.parseInt(st.nextToken());
					g[j][k] = num;
					total += num;
				}
			}
			if (total != 30) {
				sb.append(ans + " ");
				continue;
			}
			for (int j = 0; j < 6; j++) {
				if (Arrays.stream(g[j]).sum() != 5) {
					sb.append(ans + " ");
					continue loop;
				}
			}
			tmp = new int[6][3];
			vis = new boolean[6][6];
			dfs(0);
			sb.append(ans + " ");
		}
		System.out.println(sb);
	}

	static void dfs(int d) {
		if (d == 15) {
			check();
			return;
		}
		tmp[home[d]][0]++;
		tmp[away[d]][2]++;
		dfs(d + 1);
		tmp[home[d]][0]--;
		tmp[away[d]][2]--;

		tmp[home[d]][1]++;
		tmp[away[d]][1]++;
		dfs(d + 1);
		tmp[home[d]][1]--;
		tmp[away[d]][1]--;

		tmp[home[d]][2]++;
		tmp[away[d]][0]++;
		dfs(d + 1);
		tmp[home[d]][2]--;
		tmp[away[d]][0]--;
	}

	static boolean check() {
		if (ans == 1) {
			return true;
		}
		for (int i = 0; i < 6; i++) {
			for (int j = 0; j < 3; j++) {
				if (g[i][j] != tmp[i][j]) {
					return false;
				}
			}
		}
		ans = 1;
		return true;
	}
}