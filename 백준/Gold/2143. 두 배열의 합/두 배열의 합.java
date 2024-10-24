import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int t, n, m;
    static long answer = 0;
    static long[] A, B, dpA, dpB;
    static Map<Long, Long> mapA = new HashMap<>();
    static Map<Long, Long> mapB = new HashMap<>();

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());
        n = Integer.parseInt(br.readLine());
        A = new long[n];
        dpA = new long[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            if (i == 0) {
                dpA[i + 1] = A[i];
            } else {
                dpA[i + 1] = dpA[i] + A[i];
            }
        }
        m = Integer.parseInt(br.readLine());
        B = new long[m];
        dpB = new long[m + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
            if (i == 0) {
                dpB[i + 1] = B[i];
            } else {
                dpB[i + 1] = dpB[i] + B[i];
            }
        }
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                long num = dpA[i] - dpA[j];
                if (mapA.containsKey(num)) {
                    mapA.put(num, mapA.get(num) + 1);
                } else {
                    mapA.put(num, 1L);
                }
            }
        }
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j < i; j++) {
                long num = dpB[i] - dpB[j];
                if (mapB.containsKey(num)) {
                    mapB.put(num, mapB.get(num) + 1);
                } else {
                    mapB.put(num, 1L);
                }
            }
        }
        for (long i : mapA.keySet()) {
            if (mapB.containsKey(t - i)) {
                answer += mapA.get(i) * mapB.get(t - i);
            }
        }
        System.out.println(answer);
    }
}