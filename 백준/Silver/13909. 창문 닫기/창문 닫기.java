import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;

    public static void main(String[] args) throws Exception {
        n = Integer.parseInt(br.readLine());
        System.out.println((int) (Math.floor(Math.sqrt(n))));
    }
}