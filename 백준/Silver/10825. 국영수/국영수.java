import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        List<obj> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(new obj(st.nextToken(), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        arr.sort(new Comparator<obj>() {
            @Override
            public int compare(obj o1, obj o2) {
                if (o1.kor == o2.kor) {
                    if (o1.eng == o2.eng) {
                        if (o1.mat == o2.mat) {
                            return o1.name.compareTo(o2.name);
                        }
                        return Integer.compare(o2.mat, o1.mat);
                    }
                    return Integer.compare(o1.eng, o2.eng);
                }
                return Integer.compare(o2.kor, o1.kor);
            }
        });
        for (obj s:arr){
            System.out.println(s.name);
        }
    }
}

class obj {
    public String name;
    public int kor, eng, mat;

    public obj(String name, int kor, int eng, int mat) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.mat = mat;
    }
}