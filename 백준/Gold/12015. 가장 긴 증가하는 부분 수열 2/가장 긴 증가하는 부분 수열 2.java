import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, arr[];
	static List<Integer> dp = new ArrayList<>();

	public static void main(String[] args) throws Exception {
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0; i < n; i++) {
			int idx = binSearch(-1, dp.size(), arr[i]);
			dp.set(idx, arr[i]);
		}
		System.out.println(dp.size());
	}

	static int binSearch(int start, int end, int num) {
		if (dp.isEmpty()) {
			dp.add(num);
			return 0;
		}
		if (dp.get(dp.size() - 1) < num) {
			dp.add(num);
			return dp.size() - 1;
		}
		int lo = start, hi = end;
		while (lo + 1 < hi) {
			int mid = (lo + hi) / 2;
			if (num == dp.get(mid)) {
				return mid;
			}
			if (dp.get(mid) < num) {
				lo = mid;
			} else {
				hi = mid;
			}
		}
		return hi;
	}
}