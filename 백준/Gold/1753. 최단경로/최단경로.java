import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int V, E, K;
    static int INF = Integer.MAX_VALUE;
    static List<Node>[] g;
    static int[] vis;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(new StringTokenizer((br.readLine())).nextToken());
        g = new ArrayList[V + 1];

        vis = new int[V + 1];
        Arrays.fill(vis, INF);

        for (int i = 0; i <= V; i++) {
            g[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            g[u].add(new Node(v, w));
        }

        dik(K);
        for (int i = 1; i <= V; i++) {
            System.out.println(vis[i] == INF ? "INF" : vis[i]);
        }
    }

    public static void dik(int k) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        vis[k] = 0;
        pq.offer(new Node(k, 0));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int end = curNode.end;
            int dist = curNode.d;
            if (dist <= vis[end]) {
                for (Node n : g[end]) {
                    int cost = n.d + dist;
                    if (cost < vis[n.end]) {
                        vis[n.end] = cost;
                        pq.add(new Node(n.end, cost));
                    }
                }
            }
        }
    }
}

class Node implements Comparable<Node> {
    int end, d;

    public Node(int end, int d) {
        this.end = end;
        this.d = d;
    }

    @Override
    public int compareTo(Node o) {
        return this.d - o.d;
    }
}