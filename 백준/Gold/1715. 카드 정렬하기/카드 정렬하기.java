import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, ans;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.add(Integer.parseInt(br.readLine()));
        }
        if (n == 1) {
            System.out.println(0);
        } else {
            while (pq.size() > 1) {
                int tmp = pq.poll() + pq.poll();
                pq.offer(tmp);
                ans += tmp;
            }
            System.out.println(ans);
        }
    }
}