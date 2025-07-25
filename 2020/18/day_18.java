import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.function.BiFunction;

public class day_18 {
    private Map<String, BiFunction<Long, Long, Long>> operand;

    public day_18() {
        operand = new HashMap<>();
        operand.put("+", (a, b) -> a + b);
        operand.put("*", (a, b) -> a * b);
    }

    public String destroyExpressionP1(List<String> party) {
        long cur = Long.parseLong(party.remove(0));
        for (int i = 0; i < party.size(); i += 2) {
            cur = operand.get(party.get(i)).apply(cur, Long.parseLong(party.get(i + 1)));
        }
        return String.valueOf(cur);
    }

    public String destroyExpressionP2(List<String> party) {
        long cur = Long.parseLong(party.get(0));

        // Add first
        int i = 1;
        while (i < party.size()) {
            long value = Long.parseLong(party.get(i + 1));
            String c = party.get(i);
            if ("+".equals(c)) {
                cur += value;
                party.remove(i + 1);
                party.remove(i);
                party.set(i - 1, String.valueOf(cur));
            } else {
                cur = value;
                i += 2;
            }
        }

        cur = Long.parseLong(party.get(0));
        for (i = 1; i < party.size(); i += 2) {
            cur *= Long.parseLong(party.get(i + 1));
        }
        return String.valueOf(cur);
    }

    public static void main(String[] args) throws IOException {
        day_18 RyanBabel = new day_18();
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        long partOne = 0;
        long partTwo = 0;

        while ((line = reader.readLine()) != null) {
            ArrayList<String> lineList = new ArrayList<>(Arrays.asList(line.replace(" ", "").split("")));
            ArrayList<String> lineList1 = new ArrayList<>(lineList);
            ArrayList<String> lineList2 = new ArrayList<>(lineList);
            int right = 0;
            ArrayList<Integer> lBrac = new ArrayList<>();

            while (right < lineList1.size()) {
                String c = lineList1.get(right);
                switch (c) {
                    case "(" -> lBrac.add(right);
                    case ")" -> {
                        int last = lBrac.remove(lBrac.size() - 1);
                        String compressionExpressionP1 = RyanBabel
                                .destroyExpressionP1(new ArrayList<>(lineList1.subList(last + 1, right)));
                        String compressionExpressionP2 = RyanBabel
                                .destroyExpressionP2(new ArrayList<>(lineList2.subList(last + 1, right)));
                        lineList1.add(last, compressionExpressionP1);
                        lineList2.add(last, compressionExpressionP2);
                        for (int j = right + 1; j > last; j--) {
                            lineList1.remove(j);
                            lineList2.remove(j);
                        }
                        right = last;
                    }
                }
                right++;
            }

            partOne += Long.parseLong(RyanBabel.destroyExpressionP1(lineList1));
            partTwo += Long.parseLong(RyanBabel.destroyExpressionP2(lineList2));
        }
        reader.close();
        System.out.println("Part One: " + partOne);
        System.out.println("Part Two: " + partTwo);
    }
}