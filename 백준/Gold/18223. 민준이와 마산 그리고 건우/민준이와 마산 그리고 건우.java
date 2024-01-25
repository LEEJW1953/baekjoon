import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int INF = Integer.MAX_VALUE;
    static int V;
    static int E;
    static int P;

    static List<Node>[] g;
    static int[] vis;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        g = new ArrayList[V + 1];
        for (int i = 0; i <= V; i++) {
            g[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            g[a].add(new Node(b, c));
            g[b].add(new Node(a, c));
        }

        int[] vis1 = dik(1);
        int[] vis2 = dik(P);

        if ((vis1[P] + vis2[V]) == vis1[V]) {
            System.out.println("SAVE HIM");
        } else {
            System.out.println("GOOD BYE");
        }
    }

    static int[] dik(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        int[] vis = new int[V + 1];
        Arrays.fill(vis, INF);
        vis[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int end = node.end;
            int dist = node.dist;
            if (dist <= vis[end]) {
                for (Node n : g[end]) {
                    int cost = n.dist + dist;
                    if (cost < vis[n.end]) {
                        vis[n.end] = cost;
                        pq.add(new Node(n.end, cost));
                    }
                }
            }
        }
        return vis;
    }
}

class Node implements Comparable<Node> {
    int end, dist;

    public Node(int e, int d) {
        this.end = e;
        this.dist = d;
    }

    @Override
    public int compareTo(Node o) {
        return this.dist - o.dist;
    }
}