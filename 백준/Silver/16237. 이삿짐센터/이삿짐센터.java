import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	static int arr[] = new int[5], ans = 0, left;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		ans += arr[4];
		arr[4] = 0;
		for (int i = 0; i < arr[3]; i++) {
			ans++;
			if (arr[0] > 0) {
				arr[0]--;
			}
		}
		arr[3] = 0;
		for (int i = 0; i < arr[2]; i++) {
			ans++;
			if (arr[1] > 0) {
				arr[1]--;
			} else if (arr[0] > 0) {
				arr[0] -= 2;
				if (arr[0] < 0) {
					arr[0] = 0;
				}
			}
		}
		arr[2] = 0;
		for (int i = 0; i < (arr[1] / 2); i++) {
			ans++;
			if (arr[0] > 0) {
				arr[0]--;
				if (arr[0] < 0) {
					arr[0] = 0;
				}
			}
		}
		if (arr[1] % 2 == 1) {
			ans++;
			arr[0] -= 3;
			if (arr[0] < 0) {
				arr[0] = 0;
			}
		}
		arr[1] = 0;
		while (arr[0] > 0) {
			ans++;
			arr[0] -= 5;
		}
		System.out.println(ans);
	}
}