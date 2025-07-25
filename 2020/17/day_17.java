import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class day_17 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        HashMap<List<Integer>, Integer> dimension = new HashMap<>();
        Set<List<Integer>> exploreSet = new HashSet<>();
        int x = 0, y = -1, z = 0, w = 0; // Initialise coordinates

        // populate the dimension with the starting state
        while ((line = reader.readLine()) != null) {
            for (x = 0; x < line.length(); x++) {
                List<Integer> arr = Arrays.asList(x, y, z, w);
                switch (line.charAt(x)) {
                    case '#':
                        dimension.put(arr, 1);
                        break;
                    case '.':
                        dimension.put(arr, 0);
                        break;
                }
                // Add all neighbors to set to explore
                for (int dx = -1; dx <= 1; dx++) {
                    for (int dy = -1; dy <= 1; dy++) {
                        for (int dz = -1; dz <= 1; dz++) {
                            for (int dw = -1; dw <= 1; dw++) {
                                exploreSet.add(Arrays.asList(x + dx, y + dy, z + dz, w + dw));
                            }
                        }
                    }
                }
            }
            y++;
        }
        reader.close();
        // start the exploration of the neighbour dimension

        for (int part : new int[] { 2, 3 }) {
            // Deepcopy the data strucutres
            HashMap<List<Integer>, Integer> xDimension = new HashMap<>();
            for (Map.Entry<List<Integer>, Integer> entry : dimension.entrySet()) {
                List<Integer> oldKey = entry.getKey();
                List<Integer> newKey = new ArrayList<>(oldKey); // copy the key list
                Integer value = entry.getValue(); // safe to copy directly
                xDimension.put(newKey, value);
            }

            // Deep copy exploreSet
            Set<List<Integer>> xExploreSet = new HashSet<>();
            for (List<Integer> coord : exploreSet) {
                xExploreSet.add(new ArrayList<>(coord)); // copy each coordinate list
            }

            for (int ignore = 0; ignore < 6; ignore++) {
                HashMap<List<Integer>, Integer> newDimension = new HashMap<>();
                Set<List<Integer>> newExploreSet = new HashSet<>();
                for (List<Integer> coord : xExploreSet) {
                    x = coord.get(0);
                    y = coord.get(1);
                    z = coord.get(2);
                    w = coord.get(part);
                    int sumNeigh = 0;
                    for (int dx = -1; dx <= 1; dx++) {
                        for (int dy = -1; dy <= 1; dy++) {
                            for (int dz = -1; dz <= 1; dz++) {
                                for (int dw = -1; dw <= 1; dw++) {
                                    if (dx == 0 && dy == 0 && dz == 0 && dw == 0) {
                                        continue;
                                    }
                                    sumNeigh += xDimension.getOrDefault(Arrays.asList(x + dx, y + dy, z + dz, w + dw),
                                            0);
                                }
                            }
                        }
                    }
                    Integer cur = xDimension.getOrDefault(Arrays.asList(x, y, z, w), 0);
                    switch (cur) {
                        case 0:
                            if (sumNeigh == 3) {
                                cur = 1;
                            }
                            break;
                        case 1:
                            if (sumNeigh != 2 && sumNeigh != 3) {
                                cur = 0;
                            }
                    }
                    newDimension.put(Arrays.asList(x, y, z, w), cur);
                    for (int dx = -1; dx <= 1; dx++) {
                        for (int dy = -1; dy <= 1; dy++) {
                            for (int dz = -1; dz <= 1; dz++) {
                                for (int dw = -1; dw <= 1; dw++) {
                                    newExploreSet.add(Arrays.asList(x + dx, y + dy, z + dz, w + dw));
                                }
                            }
                        }
                    }
                }
                xDimension = newDimension;
                xExploreSet = newExploreSet;
            }
            int end = 0;
            for (List<Integer> key : xDimension.keySet()) {
                end += xDimension.get(key);
            }
            System.out.println("Part " + (part - 1) + ": " + end);
        }

    }
}