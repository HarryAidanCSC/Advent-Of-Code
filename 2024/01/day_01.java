import java.io.File; 
import java.io.FileNotFoundException;  
import java.util.Scanner; 
import java.util.ArrayList; 
import java.util.Collections;
import java.lang.Math;
import java.util.HashMap;

public class day_01 {
  public static void main(String[] args) {

    ArrayList<Integer> ls = new ArrayList<>();
    ArrayList<Integer> rs = new ArrayList<>();

    try {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        String[] dataArray = data.split("   ");
        int lsValue = Integer.parseInt(dataArray[0]);
        int rsValue = Integer.parseInt(dataArray[1]);
        ls.add(lsValue);
        rs.add(rsValue);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }

    Collections.sort(ls);
    Collections.sort(rs);

    // Part One
    int p1 = 0;
    int diff = 0;
    for (int i=0; i < ls.size(); i++) {
        diff = Math.abs(ls.get(i) - rs.get(i));
        p1 += diff;
    }


    // Part Two
    int p2 = 0;
    int currentVal = 0;
    HashMap<Integer, Integer> rsN = new HashMap<Integer, Integer>();
    for (int i : rs) {
        currentVal = rsN.getOrDefault(i, 0);
        rsN.put(i, currentVal + 1);
    }

    int val = 0;
    int corVal = 0;
    for (int i : ls) {
      corVal = rsN.getOrDefault(i, 0);
      val = i * corVal;
      p2 += val;
    }
    System.out.println(p1);
    System.out.println(p2);
  }
}