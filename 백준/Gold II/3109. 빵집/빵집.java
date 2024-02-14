/**
 * @author 이지원
 * @date 24.02.14
 * @link https://www.acmicpc.net/problem/3109
 * @keyword_solution 
 * DFS
 * 모든 행의 첫 번째 열 위치에서 탐색 시작
 * 갈 수 있는 경로 중 가장 위쪽부터 탐색
 * 가장 오른쪽에 도달할 때 파이프라인의 개수 +1
 * 방문 처리를 지우지 않아도 되는 이유 : 해당 위치를 지나서 마지막 열에 도달하지 못하면 다시 탐색할 필요가 없음
 * @input 
 * @output 
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
	static int r, c, ans = 0;
	static int[] dir = { -1, 0, 1 };
	static char g[][];
	static boolean vis[][];

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		g = new char[r][c];
		vis = new boolean[r][c];
		for (int i = 0; i < r; i++) {
			g[i] = br.readLine().toCharArray();
		}
		for (int i = 0; i < r; i++) {
			if (dfs(i, 0))
				ans++;
		}
		System.out.println(ans);
	}

	static boolean dfs(int x, int y) {
		vis[x][y] = true;
		if (y == (c - 1)) {
			return true;
		} else {
			for (int i = 0; i < 3; i++) {
				int nx = x + dir[i], ny = y + 1;
				if (0 <= nx && nx < r && 0 <= ny && ny < c) {
					if (g[nx][ny] == '.' && !vis[nx][ny]) {
						if (dfs(nx, ny))
							return true;
					}
				}
			}
		}
		return false;
	}
}