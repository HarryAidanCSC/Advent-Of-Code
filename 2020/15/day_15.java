import java.util.HashMap;

public class day_15 {
    public static void main(String[] args) {
        int[] finalI = { 2020, 30000000 }; // Define the final values to explore
        for (int y = 0; y < 2; y++) {
            int[] startingNumbers = { 15, 5, 1, 4, 7, 0 }; // Define input array
            int lastNumber = startingNumbers[0];
            HashMap<Integer, Integer> recentShout = new HashMap<>();

            for (int i = 1; i < finalI[y]; i++) {
                if (i < startingNumbers.length) {
                    recentShout.put(lastNumber, i);
                    lastNumber = startingNumbers[i];
                } else {
                    // Start main exec
                    Integer mappedValue = recentShout.getOrDefault(lastNumber, i);
                    recentShout.put(lastNumber, i);
                    lastNumber = i - mappedValue;
                }
            }
            System.out.println(lastNumber);
        }
    }
}