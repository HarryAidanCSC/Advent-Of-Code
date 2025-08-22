import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.regex.*;

public class day05 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("test.txt"));
        String line;
        Pattern pattern = Pattern.compile("\\d+");

        Map<Integer, Deque<Character>> stacks = new HashMap<>();

        // Enter logic
        while ((line = reader.readLine()) != null) {
            // First logical step
            if (line.indexOf('[') != -1) {
                for (int i = 1; i < line.length(); i += 4) {
                    if (line.charAt(i) != ' ') {
                        int idx = (1 + (i / 4));
                        stacks.computeIfAbsent(idx, k -> new ArrayDeque<>()).push(line.charAt(i));
                    }
                }
            }
            // Second logical step
            else if (line.contains("move")) {
                Matcher matcher = pattern.matcher(line);
                int numValues = -1;
                int fromStack = -1;
                while (matcher.find()) {
                    if (numValues < 0) numValues = Integer.parseInt(matcher.group());
                    else if (fromStack < 0) fromStack = Integer.parseInt(matcher.group());
                    else {
                        int toStack = Integer.parseInt(matcher.group());
                        for (int i = 0; i < numValues; i++){
                            stacks.get(toStack).add(stacks.get(fromStack).pollLast());
                        }
                    }
                }
            }            
        }
        for (int i = 1; i <= stacks.size(); i++) System.out.print(stacks.get(i).peekLast());
    }
}