import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int t;
    static String[][] arr = {{"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"},
            {"a", "s", "d", "f", "g", "h", "j", "k", "l", ""},
            {"z", "x", "c", "v", "b", "n", "m", "", "", ""}};
    static HashMap<String, int[]> map = new HashMap<>();
    static List<Node> res;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 10; j++) {
                int[] arr1 = {i, j};
                map.put(arr[i][j], arr1);
            }
        }

        for (int i = 0; i < t; i++) {
            res = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            int k = Integer.parseInt(st.nextToken());
            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(br.readLine());
                String tmp = st.nextToken();
                int count = 0;
                for (int x = 0; x < s.length(); x++) {
                    String c1 = s.substring(x, x + 1);
                    String c2 = tmp.substring(x, x + 1);
                    if (!c1.equals(c2)) {
                        count += Math.abs(map.get(c1)[0] - map.get(c2)[0]) + Math.abs(map.get(c1)[1] - map.get(c2)[1]);
                    }
                }
                res.add(new Node(tmp, count));
            }
            Collections.sort(res);
            for (Node n : res) {
                System.out.println(n);
            }
        }
    }
}

class Node implements Comparable<Node> {
    public String s;
    public int d;

    public Node(String s, int d) {
        this.s = s;
        this.d = d;
    }

    @Override
    public String toString() {
        return this.s + " " + this.d;
    }

    @Override
    public int compareTo(Node o) {
        if (this.d == o.d) {
            return this.s.compareTo(o.s);
        }
        return this.d - o.d;
    }
}