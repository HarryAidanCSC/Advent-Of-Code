import java.util.HashMap;

public class day_15 {
    public static void main(String[] args) {
        int[] startingNumbers = { 15, 5, 1, 4, 7, 0 }; // Define input array
        int lastNumber = startingNumbers[0];
        HashMap<Integer, Integer> recentShout = new HashMap<>();

        // Initialise default Hashmap values
        for (int i = 1; i < 2020; i++) {
            if (i < startingNumbers.length) {
                recentShout.put(lastNumber, i);
                lastNumber = startingNumbers[i];
            } else {
                // Start main exec
                Integer mappedValue = recentShout.getOrDefault(lastNumber, i);
                recentShout.put(lastNumber, i);
                // System.out.println(lastNumber + " " + i + "-" + mappedValue);
                lastNumber = i - mappedValue;
            }
        }
        System.out.println(lastNumber);
    }
}