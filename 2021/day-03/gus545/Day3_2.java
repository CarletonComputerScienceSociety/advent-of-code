import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Arrays;

public class Day3_2 {

  /**
   * Read x lines one at a time from r.  After reading x lines, output
   * the lines to w.
   * @param x the number of lines to read in
   * @param r the reader to read from
   * @param w the writer to write to
   * @throws IOException
   */
  public static void doIt(BufferedReader r, PrintWriter w)
      throws IOException {
    String line = r.readLine();
    ArrayList<String> values = new ArrayList<>();
    System.out.println(Arrays.toString(columns));
    for(String l = line; l != null; l = r.readLine()){
      values.add(l);
    }
    String oxygen = oxygenRating(values,0);
    System.out.println(binStringToInt(oxygen));
    String co2 = co2Rating(values,0);
    System.out.println(binStringToInt(co2));

    w.println(binStringToInt(oxygen)*binStringToInt(co2));



  }
  private static String oxygenRating(ArrayList<String> s, int i){
    if(s.size()==1) return s.get(0);

    ArrayList<String> ss = new ArrayList<String>();
    int count = 0;
    for(String line : s){
      if(Integer.parseInt(String.valueOf(line.charAt(i))) == 1) count++;
      else count--;
    }
    if(count>=0) count = 1;
    else count = 0;

    for(String line : s){
      if(Integer.parseInt(String.valueOf(line.charAt(i))) == count) ss.add(line);
    }

    return oxygenRating(ss, i+1);
  }
  private static int binStringToInt(String s){
    int out = 0;
    for(int i =s.length()-1; i >= 0; i--){
      int v = Integer.parseInt(String.valueOf(s.charAt(i)));
      out += v*Math.pow(2,s.length()-1-i);
    }
    return out;
  }

  private static String co2Rating(ArrayList<String> s, int i){
    if(s.size()==1) return s.get(0);

    ArrayList<String> ss = new ArrayList<String>();
    int count = 0;
    for(String line : s){
      if(Integer.parseInt(String.valueOf(line.charAt(i))) == 1) count++;
      else count--;
    }
    if(count<0) count = 1;
    else count = 0;

    for(String line : s){
      if(Integer.parseInt(String.valueOf(line.charAt(i))) == count) ss.add(line);
    }

    return co2Rating(ss, i+1);
  }

  /**
   * The driver.  Open a BufferedReader and a PrintWriter, either from System.in
   * and System.out or from filenames specified on the command line, then cl doIt on the first argument.
   * @param args
   */
  public static void main(String[] args) {
    try {
      BufferedReader r;
      PrintWriter w;
      if( args.length == 0) {
        r = new BufferedReader(new InputStreamReader(System.in));
        w = new PrintWriter(System.out);
      } else if (args.length == 1) {
        r = new BufferedReader(new FileReader(args[0]));
        w = new PrintWriter(System.out);
      } else {
        r = new BufferedReader(new FileReader(args[0]));
        w = new PrintWriter(new FileWriter(args[1]));
      }
      long start = System.nanoTime();
      doIt(r, w);
      w.flush();
      long stop = System.nanoTime();
      System.out.println("Execution time: " + 1e-9 * (stop-start));
    } catch (IOException e) {
      System.err.println(e);
      System.exit(-1);
    }
  }
}
