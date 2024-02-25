import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n, m, p[], ans, count;
    static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        p = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            p[i] = i;
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            pq.offer(new Node(a, b, c));
        }

        while (count < n - 1) {
            Node node = pq.poll();
            int a = node.from;
            int b = node.to;
            int c = node.dist;
            if (find(a) != find(b)) {
                union(a, b);
                count++;
                ans += c;
            }
        }
        System.out.println(ans);
    }

    static int find(int x) {
        if (x != p[x]) {
            p[x] = find(p[x]);
        }
        return p[x];
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x < y) {
            p[y] = x;
        } else {
            p[x] = y;
        }
    }
}

class Node implements Comparable<Node> {
    int from, to, dist;

    public Node(int a, int b, int c) {
        this.from = a;
        this.to = b;
        this.dist = c;
    }

    @Override
    public int compareTo(Node o) {
        return this.dist - o.dist;
    }
}