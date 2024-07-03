import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][][] pow;
    static int[] ans = new int[100001];

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        pow = new int[100001][5][5];
        Arrays.fill(ans, 500000);
        for (int i = 0; i < 100001; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    pow[i][j][k] = 500000;
                }
            }
        }
        pow[0][0][0] = 0;
        ans[0] = 0;
        int idx = 0;
        while (true) {
            idx++;
            int num = Integer.parseInt(st.nextToken());
            if (num == 0) {
                break;
            }
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    pow[idx][i][num] = Math.min(pow[idx][i][num], pow[idx - 1][i][j] + move(j, num));
                    pow[idx][num][j] = Math.min(pow[idx][num][j], pow[idx - 1][i][j] + move(i, num));
                }
            }
            fillAns(idx);
        }
        System.out.println(ans[idx - 1]);
    }

    // x -> y 이동 비용
    static int move(int x, int y) {
        if (x == 0) {
            if (y == 0) {
                return 0;
            }
            return 2;
        }
        if (x == y) return 1;
        return (4 + (x - y)) % 4 == 2 ? 4 : 3;
    }

    static void fillAns(int x) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                ans[x] = Math.min(ans[x], pow[x][i][j]);
            }
        }
    }
}