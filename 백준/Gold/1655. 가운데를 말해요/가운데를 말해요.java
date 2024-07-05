import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n, ans;
    // 최소 힙
    static PriorityQueue<Integer> pq1 = new PriorityQueue<>(new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2.compareTo(o1);
        }
    });
    // 최대 힙
    static PriorityQueue<Integer> pq2 = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (i == 0) {
                ans = num;
                pq1.offer(num);
                sb.append(ans).append('\n');
                continue;
            }
            if (!pq1.isEmpty() && num > pq1.peek()) {
                pq2.offer(num);
            } else {
                pq1.offer(num);
            }
            if (pq1.size() > pq2.size()) {
                while (pq1.size() > pq2.size() + 1 && !pq1.isEmpty()) {
                    pq2.offer(pq1.poll());
                }
            } else if (pq1.size() < pq2.size()) {
                while (pq1.size() < pq2.size()) {
                    pq1.offer(pq2.poll());
                }
            }
            ans = pq1.peek();
            sb.append(ans).append('\n');
        }
        System.out.println(sb);
    }
}