import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int s;
    static int n;
    static int[] switchs;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        switchs = new int[s + 1];
        for (int i = 1; i <= s; i++) {
            switchs[i] = Integer.parseInt(st.nextToken());
        }
        n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            change(gender, num);
        }
        for (int i = 1; i <= s; i++) {
            sb.append(switchs[i]).append(" ");
            if (i % 20 == 0) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    static void change(int gender, int num) {
        if (gender == 1) {
            for (int i = num; i <= s; i += num) {
                switchs[i] = Math.abs(switchs[i] - 1);
            }
        } else {
            switchs[num] = Math.abs(switchs[num] - 1);
            for (int i = 1; i <= s; i++) {
                int left = num - i;
                int right = num + i;
                if (left <= 0 || s < left || right <= 0 || s < right) {
                    break;
                }
                if (switchs[left] == switchs[right]) {
                    switchs[left] = Math.abs(switchs[left] - 1);
                    switchs[right] = Math.abs(switchs[right] - 1);
                } else {
                    return;
                }
            }
        }
    }
}