import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int T, N, x, y;
    static List<Node> list;
    static boolean[][] vis;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            list = new ArrayList<>();
            vis = new boolean[N + 2][N + 2];
            for (int i = 0; i < N + 2; i++) {
                st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                list.add(new Node(x, y));
            }
            for (int i = 0; i < N + 2; i++) {
                for (int j = 0; j < N + 2; j++) {
                    if (i != j) {
                        vis[i][j] = list.get(i).compareTo(list.get(j)) > 0;
                    }
                }
            }
            for (int k = 0; k < N + 2; k++) {
                for (int i = 0; i < N + 2; i++) {
                    for (int j = 0; j < N + 2; j++) {
                        if (!vis[i][j]) {
                            vis[i][j] = vis[i][k] && vis[k][j];
                        }
                    }
                }
            }
            if (vis[0][N + 1]) {
                sb.append("happy").append("\n");
            } else {
                sb.append("sad").append("\n");
            }
        }
        System.out.println(sb);
    }

    static class Node implements Comparable<Node> {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Node O) {
            int dist = Math.abs(this.x - O.x) + Math.abs(this.y - O.y);
            return dist <= 1000 ? 1 : -1;
        }
    }
}