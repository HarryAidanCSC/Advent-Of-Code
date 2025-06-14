import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class day_02 {
  public static void main(String[] args) {
    int p1 = 0;
    int p2 = 0;

    try {
      File obj = new File("input.txt");
      Scanner reader = new Scanner(obj);

      while (reader.hasNextLine()) {
        String data = reader.nextLine();
        String[] dataSplit = data.split(" ");
        String[] bounds = dataSplit[0].split("-");

        int boundLower = Integer.parseInt(bounds[0]);
        int boundUpper = Integer.parseInt(bounds[1]);
        char targetChar = dataSplit[1].charAt(0);
        String password = dataSplit[2];

        // Part 1
        int charCount = 0;
        for (char c : password.toCharArray()) {
          if (c == targetChar) {
            charCount++;
          }
        }

        if (charCount >= boundLower & charCount <= boundUpper) {
          p1++;
        }
        // Part 2
        char lowerChar = password.charAt(boundLower - 1);
        char upperChar = password.charAt(boundUpper - 1);
        if (lowerChar != upperChar && lowerChar == targetChar | upperChar == targetChar) {
          p2++;
        }

      }
      reader.close();
      System.out.println(p1);
      System.out.println(p2);
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred");
      e.printStackTrace();
    }
  }
}
