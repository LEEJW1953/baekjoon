import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, total, mst;
    static int[] vis;
    static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        vis = new int[n];
        for (int i = 0; i < n; i++) {
            vis[i] = i;
            String lan = br.readLine();
            for (int j = 0; j < n; j++) {
                char c = lan.charAt(j);
                if (c == '0') {
                    continue;
                }
                if ('a' <= c) {
                    int cost = c - 'a' + 1;
                    total += cost;
                    pq.offer(new Node(i, j, cost));
                } else if ('A' <= c) {
                    int cost = c - 'A' + 27;
                    total += cost;
                    pq.offer(new Node(i, j, cost));
                }
            }
        }
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int from = node.x;
            int to = node.y;
            int cost = node.cost;
            if (union(from, to)) {
                mst += cost;
            }
        }
        for (int i = 0; i < n; i++) {
            if (find(vis[i]) != 0) {
                System.out.println("-1");
                System.exit(0);
            }
        }
        System.out.println(total - mst);
    }

    static int find(int x) {
        if (x != vis[x]) {
            vis[x] = find(vis[x]);
        }
        return vis[x];
    }

    static boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        }
        if (x < y) {
            vis[y] = x;
        } else {
            vis[x] = y;
        }
        return true;
    }

    static class Node implements Comparable<Node> {
        int x, y, cost;

        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }
}