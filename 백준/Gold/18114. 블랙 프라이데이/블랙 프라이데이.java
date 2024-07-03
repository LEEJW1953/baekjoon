import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, c, w[];

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        w = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num == c) {
                System.out.println(1);
                System.exit(0);
            }
            w[i] = num;
        }
        Arrays.sort(w);
        for (int i = 0; i < n; i++) {
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                int num1 = w[i] + w[left];
                int num2 = w[i] + w[right];
                int num3 = w[left] + w[right];
                int num4 = w[i] + w[left] + w[right];
                if (num1 == c || num2 == c || num3 == c || num4 == c) {
                    System.out.println(1);
                    System.exit(0);
                }
                if (num4 < c) {
                    left++;
                }
                if (num4 > c) {
                    right--;
                }
            }
        }
        System.out.println(0);
    }
}