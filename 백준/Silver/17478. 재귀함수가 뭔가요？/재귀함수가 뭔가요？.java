import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static int t;
	static String indent = "____";

	public static void main(String[] args) throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		t = Integer.parseInt(st.nextToken());
		sb.append("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
		function(t);
		System.out.println(sb);
	}

	static void function(int n) {
		if (n == 0) {
			insertIndent(t - n);
			sb.append("\"재귀함수가 뭔가요?\"\n");
			insertIndent(t - n);
			sb.append("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
			insertIndent(t - n);
			sb.append("라고 답변하였지.\n");
			return;
		}
		insertIndent(t - n);
		sb.append("\"재귀함수가 뭔가요?\"\n");
		insertIndent(t - n);
		sb.append("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
		insertIndent(t - n);
		sb.append("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
		insertIndent(t - n);
		sb.append("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
		function(n - 1);
		insertIndent(t - n);
		sb.append("라고 답변하였지.\n");
	}

	static void insertIndent(int n) {
		for (int i = 0; i < n; i++) {
			sb.append(indent);
		}
	}
}