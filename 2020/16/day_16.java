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
        HashMap<Integer, List<Integer>> nearby = new HashMap<>();
        List<Integer> personal = new ArrayList<>();

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
                    String[] personalNumbers = line.split(",");
                    for (String personalNumber : personalNumbers) {
                        personal.add(Integer.parseInt(personalNumber));
                    }

                    // Placeholder
                    break;
                case "nearby":
                    int pos = 0;
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
                        } else {
                            nearby.computeIfAbsent(pos++, k -> new ArrayList<>()).add(num);
                        }
                    }
                    break;
            }
        }
        reader.close();
        System.out.println(partOne);

        HashMap<String, List<Integer>> possibleMap = new HashMap<>();
        // Loop through cond map to find which idx is each condition
        for (String key : keys) {
            List<Integer> conditions = condMap.get(key);
            for (int x = 0; x < nearby.size(); x++) { // Enter nearby index
                List<Integer> values = nearby.get(x);
                boolean isGood = true;

                for (int num : values) {
                    boolean isNumChill = false;
                    for (int v = 1; v < conditions.size(); v += 2) {
                        if (num >= conditions.get(v - 1) && num <= conditions.get(v)) {
                            isNumChill = true;
                            break;
                        }
                    }
                    if (!isNumChill) {
                        isGood = false;
                        break;
                    }
                }
                if (isGood) {
                    possibleMap.computeIfAbsent(key, k -> new ArrayList<>()).add(x);
                }
            }
        }
        // Find only correct combinaton
        List<Integer> destinations = new ArrayList<>();
        List<Map.Entry<String, List<Integer>>> entries = new ArrayList<>(possibleMap.entrySet());
        entries.sort(Comparator.comparingInt(entry -> entry.getValue().size()));
        Set<Integer> exclusion = new HashSet<>();
        for (Map.Entry<String, List<Integer>> entry : entries) {
            // System.out.println(entry.getKey() + " => " + entry.getValue());
            for (int num : entry.getValue()) {
                if (!exclusion.contains(num)) {
                    exclusion.add(num);
                    if (entry.getKey().startsWith("departure ")) {
                        destinations.add(personal.get(num));
                    }
                }
            }
        }
        long partTwo = 1;
        for (long letsNotForgetItsBeenRaining : destinations) {

            partTwo *= letsNotForgetItsBeenRaining;
        }
        System.out.println(partTwo);

    }
}