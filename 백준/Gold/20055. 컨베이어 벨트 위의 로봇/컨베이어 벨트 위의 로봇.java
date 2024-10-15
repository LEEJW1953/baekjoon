import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, k, count = 0, ans = 0;
    static int[][] belt;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        belt = new int[2 * n][2];
        for (int i = 0; i < 2 * n; i++) {
            int num = Integer.parseInt(st.nextToken());
            belt[i][0] = num;
            if (num == 0) {
                count++;
            }
        }
        while (count < k) {
            rotate();
            move();
            if (0 < belt[0][0] && belt[0][1] == 0) {
                belt[0][0]--;
                belt[0][1] = 1;
                if (belt[0][0] == 0) {
                    count++;
                }
            }
            ans++;
        }
        System.out.println(ans);
    }

    static void rotate() {
        int a = belt[2 * n - 1][0];
        int b = belt[2 * n - 1][1];
        for (int i = 2 * n - 1; i > 0; i--) {
            belt[i][0] = belt[i - 1][0];
            belt[i][1] = belt[i - 1][1];
            if (i == n - 1) {
                belt[i][1] = 0;
            }
        }
        belt[0][0] = a;
        belt[0][1] = b;
    }

    static void move() {
        for (int i = n - 1; i > 0; i--) {
            if (belt[i - 1][1] == 1 && belt[i][0] > 0 && belt[i][1] == 0) {
                belt[i - 1][1] = 0;
                belt[i][0]--;
                belt[i][1] = 1;
                if (belt[i][0] == 0) {
                    count++;
                }
            }
        }
        if (belt[n - 1][1] == 1) {
            belt[n - 1][1] = 0;
        }
    }
}