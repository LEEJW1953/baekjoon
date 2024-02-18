import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n;
    static char[][] arr;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        arr = new char[n][n];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }
        quadTree(0, 0, n);
        System.out.println(sb);
    }

    static void quadTree(int x, int y, int s) {
        char num = arr[x][y];
        if (check(x, y, s)) {
            sb.append(num);
            return;
        }
        sb.append("(");
        int half = s / 2;
        quadTree(x, y, half);
        quadTree(x, y + half, half);
        quadTree(x + half, y, half);
        quadTree(x + half, y + half, half);
        sb.append(")");
    }

    static boolean check(int x, int y, int s) {
        char num = arr[x][y];
        for (int i = x; i < x + s; i++) {
            for (int j = y; j < y + s; j++) {
                if (arr[i][j] != num) {
                    return false;
                }
            }
        }
        return true;
    }
}