import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int ans = 0;
        int[][] res = new int[n][2];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int[] arr = new int[l];
            int[] dp = new int[l + 1];
            int total = Integer.MIN_VALUE;
            int start = 0;
            int end = 0;
            int count = Integer.MAX_VALUE;
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < l; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
                dp[j + 1] = dp[j] + arr[j];
            }
            for (int j = 0; j < l + 1; j++) {
                for (int k = j + 1; k < l + 1; k++) {
                    int tmp = dp[k] - dp[j];
                    if (tmp > total) {
                        total = tmp;
                        start = j + 1;
                        end = k;
                        count = end - start;
                    } else if (tmp == total) {
                        int count1 = k - j - 1;
                        if (count1 < count) {
                            count = count1;
                            start = j + 1;
                            end = k;
                        }
                    }
                }
            }
            ans += total;
            res[i][0] = start;
            res[i][1] = end;
        }
        System.out.println(ans);
        for (int i = 0; i < n; i++) {
            System.out.print(res[i][0]);
            System.out.print(" ");
            System.out.println(res[i][1]);
        }
    }
}