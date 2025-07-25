import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class day_19 {
    private static boolean allAB(ArrayList<String> st) {
        for (String s : st) {
            if (!s.matches("a|b")) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        Map<String, ArrayList<ArrayList<String>>> map = new HashMap<>();
        HashSet<String> values = new HashSet<>();

        // populate the dimension with the starting state
        while ((line = reader.readLine()) != null) {
            // System.out.println(line);
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
        // Start with number 0 and build up a stack
        ArrayList<ArrayList<String>> stack = new ArrayList<>();
        stack.add(map.get("0").get(0));
        HashSet<String> dutty = new HashSet<>();

        while (!stack.isEmpty()) {
            ArrayList<String> top = stack.remove(stack.size() - 1);
            if (allAB(top)) {
                dutty.add(String.join("", top));
                continue;
            }

            ArrayList<ArrayList<String>> a = new ArrayList<>();
            a.add(new ArrayList<>());
            for (String i : top) {

                ArrayList<ArrayList<String>> temp = new ArrayList<>();
                if (i.matches("\\d+")) {
                    temp = map.get(i);
                } else {
                    temp.add(new ArrayList<>(List.of(i)));
                }
                ArrayList<ArrayList<String>> b = new ArrayList<>();
                for (ArrayList<String> x : a) {
                    for (ArrayList<String> y : temp) {
                        ArrayList<String> z = new ArrayList<>(x);
                        z.addAll(y);
                        b.add(z);
                    }
                }
                a = b;
            }
            // Add back onto the stack
            for (ArrayList<String> x : a) {
                stack.add(x);
            }
        }
        // Part One
        HashSet<String> intersection = new HashSet<>(dutty);
        intersection.retainAll(values);
        System.out.println(intersection.size());
    }

}
