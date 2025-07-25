import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class day_19 {

    private static List<Integer> match(Map<String, ArrayList<ArrayList<String>>> rules, String ruleNum, String message,
            int index) {
        ArrayList<ArrayList<String>> options = rules.get(ruleNum);
        List<Integer> result = new ArrayList<>();
        for (ArrayList<String> option : options) {
            List<Integer> idxs = new ArrayList<>();
            idxs.add(index);
            for (String token : option) {
                List<Integer> newIdxs = new ArrayList<>();
                for (int idx : idxs) {
                    if (token.equals("a") || token.equals("b")) {
                        if (idx < message.length() && message.charAt(idx) == token.charAt(0)) {
                            newIdxs.add(idx + 1);
                        }
                    } else {
                        newIdxs.addAll(match(rules, token, message, idx));
                    }
                }
                idxs = newIdxs;
            }
            result.addAll(idxs);
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        Map<String, ArrayList<ArrayList<String>>> map = new HashMap<>();
        HashSet<String> values = new HashSet<>();

        // populate the dimension with the starting state
        while ((line = reader.readLine()) != null) {
            if (line.contains(":")) {
                String key = line.substring(0, line.indexOf(":"));
                String value = line.substring(line.indexOf(":") + 2).replace("\"", "");

                ArrayList<ArrayList<String>> groups = new ArrayList<>();

                for (String part : value.split(" \\| ")) {
                    ArrayList<String> sublist = new ArrayList<>(List.of(part.split(" ")));
                    groups.add(sublist);
                }

                map.put(key, groups);
            } else if (line.matches("[ab]+")) {
                values.add(line);
            }
        }
        reader.close();

        // PART 2 MODIFICATION: update rules 8 and 11
        if (map.containsKey("8")) {
            ArrayList<ArrayList<String>> rule8 = new ArrayList<>();
            rule8.add(new ArrayList<>(List.of("42")));
            rule8.add(new ArrayList<>(List.of("42", "8")));
            map.put("8", rule8);
        }
        if (map.containsKey("11")) {
            ArrayList<ArrayList<String>> rule11 = new ArrayList<>();
            rule11.add(new ArrayList<>(List.of("42", "31")));
            rule11.add(new ArrayList<>(List.of("42", "11", "31")));
            map.put("11", rule11);
        }

        int count = 0;
        for (String msg : values) {
            List<Integer> res = match(map, "0", msg, 0);
            if (res.contains(msg.length())) {
                count++;
            }
        }
        System.out.println(count);
    }

}
