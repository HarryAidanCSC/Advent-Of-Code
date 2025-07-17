import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day_14 {
    public static void main(String[] args) throws IOException {
        // Define bmask
        Map<Integer, Character> bitmask = new LinkedHashMap<>();
        char[] skullEmoji = new char[36];
        // Define mem
        Map<Long, Long> mem = new LinkedHashMap<>();
        Map<Long, Long> meme = new LinkedHashMap<>();

        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            // Do the map logic
            if (line.startsWith("mask")) {
                bitmask.clear();
                Arrays.fill(skullEmoji, '0');
                String itsClobberingTime = line.substring(7);
                for (Integer i = 0; i < itsClobberingTime.length(); i++) {
                    if (itsClobberingTime.charAt(i) != 'X') {
                        bitmask.put(i, itsClobberingTime.charAt(i));
                    }
                    skullEmoji[i] = itsClobberingTime.charAt(i);
                }
            } else {
                Matcher matcher = Pattern.compile("\\[(.*?)\\]").matcher(line);
                matcher.find();
                String idx = matcher.group(1);
                long indx = Long.parseLong(idx);

                // Fixed: Correct parsing of value after '='
                long baby = Long.parseLong(line.substring(line.indexOf('=') + 2));

                // Part One: Apply mask to VALUE
                String binaryBaby = Long.toBinaryString(baby);
                String babyPadding = String.format("%36s", binaryBaby).replace(' ', '0');
                char[] tickleMonster = babyPadding.toCharArray();

                // Apply bitmask to value
                for (Map.Entry<Integer, Character> entry : bitmask.entrySet()) {
                    int pos = entry.getKey();
                    char bit = entry.getValue();
                    tickleMonster[pos] = bit;
                }

                String imFromWakina = new String(tickleMonster);
                mem.put(indx, Long.parseLong(imFromWakina, 2));

                // Part Two: Apply mask to ADDRESS
                String flintAndSteel = Long.toBinaryString(indx);
                String chickenJockey = String.format("%36s", flintAndSteel).replace(' ', '0');

                Deque<String> stack = new ArrayDeque<>();
                stack.push("");

                while (!stack.isEmpty()) {
                    String s = stack.pop();
                    int len = s.length();
                    if (len > 35) {
                        meme.put(Long.parseUnsignedLong(s, 2), baby);
                        continue;
                    }
                    char batman = skullEmoji[len];
                    switch (batman) {
                        case '0' -> {
                            s = s + chickenJockey.charAt(len);
                            stack.add(s);
                        }
                        case '1' -> {
                            s = s + "1";
                            stack.add(s);
                        }
                        case 'X' -> {
                            stack.add(s + "1");
                            stack.add(s + "0");
                        }
                    }
                }
            }
        }
        reader.close();

        long partOne = 0;
        for (Map.Entry<Long, Long> entry : mem.entrySet()) {
            partOne += entry.getValue();
        }

        long partTwo = 0;
        for (Map.Entry<Long, Long> entry : meme.entrySet()) {
            partTwo += entry.getValue();
        }

        // Print Part One
        System.err.println("Part One: " + partOne);
        System.err.println("Part Two: " + partTwo);
    }
}