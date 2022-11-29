import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) { // iterates through all tokens in stdin
            String token = st.nextToken(); // you can pass a string parameter as a delimiter to tokenize. ex. ","
            // System.out.println(token);
        }

    }
}