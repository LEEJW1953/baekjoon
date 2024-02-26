import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, ans = 0, start, end;
	static List<Project> dates = new ArrayList<Project>();

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int a = 100 * Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
			int b = 100 * Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
			dates.add(new Project(a, b));
		}
		Collections.sort(dates);
		int idx = 0;
		if (dates.get(0).end > 1130) {
			while (end <= 1130) {
				idx++;
				if (ans == 0) {
					for (int i = 0; i < N; i++) {
						Project p = dates.get(i);
						if (p.start <= 301) {
							ans++;
							start = p.start;
							end = p.end;
							break;
						}
					}
				} else {
					for (int i = 0; i < N; i++) {
						Project p = dates.get(i);
						if (p.start <= end) {
							ans++;
							start = p.start;
							end = p.end;
							break;
						}
					}
				}
				if (idx >= 100000) {
					ans = 0;
					break;
				}
			}
			System.out.println(ans);
		} else {
			System.out.println(0);
		}
	}
}

class Project implements Comparable<Project> {
	int start, end;

	public Project(int a, int b) {
		this.start = a;
		this.end = b;
	}

	public int compareTo(Project o) {
		if (this.end == o.end) {
			return o.start - this.start;
		}
		return o.end - this.end;
	}
}