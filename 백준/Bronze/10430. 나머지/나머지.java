import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int [] arr = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for(int i = 0 ; i < 3 ; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int a = arr[0];
        int b = arr[1];
        int c = arr[2];

        sb.append((a+b)%c).append('\n');
        sb.append(((a % c) + (b % c)) % c).append('\n');
        sb.append( (a*b)%c).append('\n');
        sb.append(((a % c) * (b % c)) % c).append('\n');


        System.out.println(sb);
    }
}