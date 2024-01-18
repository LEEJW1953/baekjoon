import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static String[][] g;
    static int minn = Integer.MAX_VALUE;
    static int maxx = Integer.MIN_VALUE;
    static int[] dx = {1, 0};
    static int[] dy = {0, 1};

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        g = new String[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                g[i][j] = st.nextToken();
            }
        }

        String[] arr = new String[2 * n - 1];
        arr[0] = g[0][0];
        dfs(0, 0, arr, 1);
        System.out.println(maxx + " " + minn);
    }

    public static void dfs(int x, int y, String[] arr, int d) {
        if (x == n - 1 && y == n - 1) {
            int tmp = cal(arr);
            minn = Math.min(minn, tmp);
            maxx = Math.max(maxx, tmp);
            return;
        }

        for (int i = 0; i < 2; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if ((0 <= nx) && (nx < n) && (0 <= ny) && (ny < n)) {
                arr[d] = g[nx][ny];
                dfs(nx, ny, arr, d + 1);
                arr[d] = "";
            }
        }
    }

    public static int cal(String[] arr) {
        int total = Integer.parseInt(arr[0]);
        for (int i = 1; i < 2 * n - 1; i += 2) {
            switch (arr[i]) {
                case "+":
                    total += Integer.parseInt(arr[i + 1]);
                    break;
                case "-":
                    total -= Integer.parseInt(arr[i + 1]);
                    break;
                case "*":
                    total *= Integer.parseInt(arr[i + 1]);
                    break;
            }
        }
        return total;
    }
}