import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.*;

public class day_16 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        String type = "field";
        HashMap<String, List<Integer>> condMap = new HashMap<>();
        int partOne = 0;
        Set<String> keys = new HashSet<>();

        // Enter logic
        while ((line = reader.readLine()) != null) {
            if (line.length() == 0)
                continue; // Ignore empty lines
            switch (type) {
                case "field":
                    if (line.equals("your ticket:")) { // Move onto next logical chunk
                        type = "personal";
                        break;
                    }
                    String fieldType = line.substring(0, line.indexOf(":"));
                    List<Integer> numbers = new ArrayList<>();
                    Pattern pattern = Pattern.compile("\\d+");
                    Matcher matcher = pattern.matcher(line);

                    while (matcher.find()) {
                        numbers.add(Integer.parseInt(matcher.group()));
                    }
                    condMap.computeIfAbsent(fieldType, k -> new ArrayList<>()).addAll(numbers);
                    break;
                case "personal":
                    if (line.equals("nearby tickets:")) { // Move onto next logical chunk
                        type = "nearby";
                        keys = condMap.keySet();
                        break;
                    }
                    // Placeholder
                    break;
                case "nearby":
                    String[] nearbyNumbers = line.split(",");
                    for (String nearbyNumber : nearbyNumbers) {
                        int num = Integer.parseInt(nearbyNumber);
                        // Enter the hashmap loop
                        boolean isGood = false;
                        for (String key : keys) {
                            List<Integer> values = condMap.get(key);
                            for (int v = 1; v < values.size(); v += 2) {
                                if (num >= values.get(v - 1) && num <= values.get(v)) {
                                    isGood = true;
                                    break;
                                }
                            }
                            if (isGood) {
                                break;
                            }
                        }
                        if (!isGood) {
                            partOne += num;
                        }
                    }
                    break;
            }
        }
        reader.close();
        System.out.println(partOne);
    }
}