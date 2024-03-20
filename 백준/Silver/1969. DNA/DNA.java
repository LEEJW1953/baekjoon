import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int n, m, dis;
	static String s, dna[] = { "A", "C", "G", "T" }, nuc[], ans = "";

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		nuc = new String[n];
		for (int i = 0; i < n; i++) {
			nuc[i] = br.readLine();
		}
		for (int j = 0; j < m; j++) {
			int[] count = new int[4];
			for (int i = 0; i < n; i++) {
				switch (nuc[i].charAt(j)) {
				case 'A':
					count[0]++;
					break;
				case 'C':
					count[1]++;
					break;
				case 'G':
					count[2]++;
					break;
				case 'T':
					count[3]++;
					break;
				}
			}
			int max = 0, idx = 0, total = 0;
			for (int k = 0; k < 4; k++) {
				total += count[k];
				if (max < count[k]) {
					max = count[k];
					idx = k;
				}
			}
			ans += dna[idx];
			dis += total - max;
		}
		System.out.println(ans);
		System.out.println(dis);
	}
}