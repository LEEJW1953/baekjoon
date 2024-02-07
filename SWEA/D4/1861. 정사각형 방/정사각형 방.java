/**
 * @author 이지원
 * @date 2024.02.07
 * @link https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY0LFFoqrIIDFAXz&contestProbId=AV5LtJYKDzsDFAXc&probBoxId=AY13IwlKMEcDFAWX&type=PROBLEM&problemBoxTitle=0205%EC%A3%BC&problemBoxCnt=4
 * @keyword_solution 모든 좌표에서 BFS
 * @input N*N의 모든 좌표 값이 다른 이차원배열
 * @output 이동할 수 있는 최대 개수의 방의 번호와 이동할 수 있는 방의 개수
 * 이동할 수 있는 방의 개수가 같을 경우 번호가 가장 작은 방
 * @time_complex 
 * @perf 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int INF = Integer.MAX_VALUE;
	static int t, n, room, validRooms;
	static int[][] g;
	static boolean[][] vis;
	static int[] dx = new int[] { 0, 1, 0, -1 };
	static int[] dy = new int[] { 1, 0, -1, 0 };

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		t = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= t; i++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			g = new int[n][n];
			vis = new boolean[n][n];
			room = 10000000;
			validRooms = 0;
			for (int j = 0; j < n; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k = 0; k < n; k++) {
					g[j][k] = Integer.parseInt(st.nextToken());
				}
			}

			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					if (!vis[j][k]) {
						bfs(j, k, g[j][k]);
					}
				}
			}
			System.out.println("#" + i + " " + room + " " + validRooms);
		}
	}

	static void bfs(int x, int y, int num) {
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] { x, y });
		vis[x][y] = true;
		List<Integer> res = new ArrayList<>();
		while (!q.isEmpty()) {
			int[] node = q.poll();
			int xx = node[0];
			int yy = node[1];
			res.add(g[xx][yy]);
			for (int i = 0; i < 4; i++) {
				int nx = xx + dx[i];
				int ny = yy + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					if (!vis[nx][ny] && (Math.abs(g[nx][ny] - g[xx][yy]) == 1)) {
						q.offer(new int[] { nx, ny });
						vis[nx][ny] = true;
					}
				}
			}
		}
		Collections.sort(res);
		int rooms = res.size();
		if (validRooms == rooms) {
			if (res.get(0) < room) {
				room = res.get(0);
			}
		} else if (validRooms < rooms) {
			room = res.get(0);
			validRooms = rooms;
		}
	}
}