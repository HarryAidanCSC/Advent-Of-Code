import java.io.File; 
import java.io.FileNotFoundException;  
import java.util.Scanner; 
import java.util.HashSet;

public class day_01 {
  public static void main(String[] args) {

    HashSet<Integer> ls = new HashSet<Integer>();

    try {
      File obj = new File("input.txt");
      Scanner reader = new Scanner(obj);
      while (reader.hasNextLine()) {
        String data = reader.nextLine();
        int lsValue = Integer.parseInt(data);
        ls.add(lsValue);
      }
      reader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    // Part One
    int diff = 0;
    int p1 = 0;
    HashSet<Integer> seen = new HashSet<Integer>();
    for (int i : ls) {
        if (seen.contains(i)){
            continue;
        } else {
            diff = 2020 - i;
            if (ls.contains(diff)) {
                p1 += (diff * i);
                seen.add(diff);
            }
        }
    }
    System.out.println(p1);


    // Part Two
    boolean breakflag = false;
    int cur1, cur2, cur3 = 0;
    for (int i : ls) {
        cur1 = 2020 - i;
        for (int j : ls){
            if (breakflag){
                break;
            }
            if (j == i){
                continue;
            }
            cur2 = cur1 - j;
            for (int n : ls){
                if (breakflag){
                    break;
                }
                if (n == i || n == j){
                    continue;
                }
                cur3 = cur2 - n;
                if (cur3 == 0){
                    System.out.println(i*j*n);
                    breakflag = true;
                    break;
                }
            }
        }
    }
  }
}
