import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int r, c;
    static String[][] board;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static boolean[] vis = new boolean[26];
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        board = new String[r][c];

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            String[] input = st.nextToken().split("");
            for (int j = 0; j < c; j++) {
                board[i][j] = input[j];
            }
        }
        vis[board[0][0].charAt(0) - 65] = true;
        dfs(0, 0, 1);
        System.out.println(ans);
    }

    static void dfs(int x, int y, int d) {
        ans = Math.max(ans, d);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                if (!vis[board[nx][ny].charAt(0) - 65]) {
                    vis[board[nx][ny].charAt(0) - 65] = true;
                    dfs(nx, ny, d + 1);
                    vis[board[nx][ny].charAt(0) - 65] = false;
                }
            }
        }
    }
}