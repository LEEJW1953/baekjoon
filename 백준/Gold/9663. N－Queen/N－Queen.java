import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n;
    static int ans = 0;
    static List<Integer> queens = new ArrayList<>(); // index 가 퀸의 x좌표, 값이 y좌표

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        queen(0);
        System.out.println(ans);
    }

    static void queen(int x) {
        if (x == n) {
            ans++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (check(i)) {
                queens.add(i);
                queen(x + 1);
                queens.remove(queens.size() - 1);
            }
        }
    }

    static boolean check(int x) {
        int s = queens.size();
        for (int i = 0; i < s; i++) {
            int q = queens.get(i);
            if (q == x || (i - q) == (s - x) || (i + q) == (s + x)) {
                return false;
            }
        }
        return true;
    }
}