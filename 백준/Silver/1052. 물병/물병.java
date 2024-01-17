import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static int k;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int tmp = 0;
        if (k == 1) {
            tmp = (int) Math.ceil(Math.log(n) / Math.log(2)) - 1;
            System.out.println((int) Math.pow(2, tmp + 1) - n);
        } else {
            for (int i = 0; i < k - 1; i++) {
                tmp = (int) Math.floor(Math.log(n) / Math.log(2));
                n -= (int) Math.pow(2, tmp);
            }
            tmp = (int) Math.ceil(Math.log(n) / Math.log(2)) - 1;
            System.out.println((int) Math.pow(2, tmp + 1) - n);
        }
    }
}