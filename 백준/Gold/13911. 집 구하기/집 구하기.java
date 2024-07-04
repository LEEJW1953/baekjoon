import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int v, e, M, x, S, y;
    static long INF = 4000000000L, ans = INF;
    static List<Node>[] g;
    static boolean[] isHouse;
    static List<Integer> mcDonald = new ArrayList<>();
    static List<Integer> starbucks = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        g = new ArrayList[v + 3];
        isHouse = new boolean[v + 3];
        Arrays.fill(isHouse, true);
        for (int i = 0; i <= v + 2; i++) {
            g[i] = new ArrayList<>();
        }
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            g[u].add(new Node(v, w));
            g[v].add(new Node(u, w));
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int num = Integer.parseInt(st.nextToken());
            mcDonald.add(num);
            g[v + 1].add(new Node(num, 0));
            isHouse[num] = false;
        }
        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < S; i++) {
            int num = Integer.parseInt(st.nextToken());
            starbucks.add(num);
            g[v + 2].add(new Node(num, 0));
            isHouse[num] = false;
        }
        long[] visM = dijkstra(v + 1);
        long[] visS = dijkstra(v + 2);
        for (int i = 1; i <= v; i++) {
            if (isHouse[i]) {
                if (visM[i] > x || visS[i] > y) continue;
                ans = Math.min(ans, visM[i] + visS[i]);
            }
        }
        System.out.println(ans >= INF ? -1 : ans);
    }

    static long[] dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        long[] vis = new long[v + 3];
        Arrays.fill(vis, INF);
        vis[start] = 0;
        for (int i = 0; i < g[start].size(); i++) {
            Node node = g[start].get(i);
            pq.offer(new Node(node.v, node.w));
            vis[node.v] = Math.min(vis[node.v], node.w);
        }
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            for (int i = 0; i < g[node.v].size(); i++) {
                Node next = g[node.v].get(i);
                long cost = node.w + next.w;
                if (cost > vis[next.v]) continue;
                pq.offer(new Node(next.v, cost));
                vis[next.v] = cost;
            }
        }
        return vis;
    }
}

class Node implements Comparable<Node> {
    int v;
    long w;

    Node(int v, long w) {
        this.v = v;
        this.w = w;
    }

    @Override
    public int compareTo(Node o) {
        return Long.compare(this.w, o.w);
    }
}