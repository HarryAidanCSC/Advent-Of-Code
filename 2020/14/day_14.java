import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day_14 {
    public static void main(String[] args) throws IOException {
        // Define memory
        Map<Integer, Character> bitmask = new LinkedHashMap<>();
        // Define bitmask
        Map<Integer, Long> mem = new LinkedHashMap<>();

        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            // Do the map logic
            if (line.startsWith("mask")) {
                bitmask.clear();
                String sliced = line.substring(7);
                for (Integer i = 0; i < sliced.length(); i++) {
                    if (sliced.charAt(i) != 'X') {
                        bitmask.put(i, sliced.charAt(i));
                    }
                }
            } else {
                Matcher matcher = Pattern.compile("\\[(.*?)\\]").matcher(line);
                matcher.find();
                String idx = matcher.group(1);
                int indx = Integer.parseInt(idx);
                // Define the value
                int baby = Integer.parseInt(line.substring(8 + idx.length()));
                String binaryBaby = Integer.toBinaryString(baby);
                String babyPadding = String.format("%36s", binaryBaby).replace(' ', '0');
                System.out.println(babyPadding);
                // Conver to array
                char[] tickleMonster = babyPadding.toCharArray();
                // Apply bitmask
                for (Map.Entry<Integer, Character> entry : bitmask.entrySet()) {
                    int pos = entry.getKey();
                    char bit = entry.getValue();
                    tickleMonster[pos] = bit;
                }
                // Back to a 36 bit int
                String imFromWakina = new String(tickleMonster);
                System.err.println(imFromWakina);

                mem.put(indx, Long.parseLong(imFromWakina, 2));
                System.err.println(Long.parseLong(imFromWakina, 2));
            }
        }
        reader.close();
        long partOne = 0;
        for (Map.Entry<Integer, Long> entry : mem.entrySet()) {
            partOne += entry.getValue();
        }
        // Print Part One
        System.err.println(partOne);
    }
}