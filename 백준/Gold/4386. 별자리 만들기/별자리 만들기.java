import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, count, p[];
    static double ans;
    static Node[] Nodes;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        p = new int[n + 1];
        Arrays.fill(p, -1);
        Nodes = new Node[n + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            double a = Double.parseDouble(st.nextToken());
            double b = Double.parseDouble(st.nextToken());
            Nodes[i] = new Node(a, b);
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                pq.offer(new Edge(i, j));
            }
        }

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            int a = edge.from;
            int b = edge.to;
            double c = edge.dist;
            if (find(a) != find(b)) {
                union(a, b);
                count++;
                ans += (double) Math.round(c * 100) / 100;
            }
        }
        System.out.println((double) Math.round(ans * 100) / 100);
    }

    static int find(int x) {
        if (p[x] < 0) {
            return x;
        }
        return p[x] = find(p[x]);
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

class Node {
    double x, y;

    Node(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

class Edge implements Comparable<Edge> {
    int from, to;
    double dist;

    public Edge(int x, int y) {
        this.from = x;
        this.to = y;
        double dx = Main.Nodes[x].x - Main.Nodes[y].x;
        double dy = Main.Nodes[x].y - Main.Nodes[y].y;
        this.dist = Math.sqrt(dx * dx + dy * dy);
    }

    public int compareTo(Edge o) {
        return Double.compare(this.dist, o.dist);
    }
}