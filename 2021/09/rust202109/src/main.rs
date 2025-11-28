use std::collections::HashSet;
use std::fs;
use std::hash::Hash;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i32>> = file
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
        .collect();

    // Part One
    let mut p1 = 0;
    let directions = [(0, 1), (1, 0), (-1, 0), (0, -1)];

    let mut nines_shining: HashSet<(usize, usize)> = HashSet::new();

    for (i, row) in lines.iter().enumerate() {
        for (j, value) in row.iter().enumerate() {
            let mut skip = false;

            // p2 logic
            if value == &9 {
                nines_shining.insert((i, j));
            }
            for (di, dj) in directions.iter() {
                let (ni, nj) = (i as i32 + di, j as i32 + dj);
                if let Some(neighbour) = lines.get(ni as usize).and_then(|r| r.get(nj as usize)) {
                    if neighbour <= value {
                        skip = true;
                        break;
                    }
                }
            }
            if !skip {
                p1 += 1 + value;
            }
        }
    }

    // P2
    let mut basins: Vec<i64> = vec![];
    let mut universe_seen = nines_shining.clone();
    for (i, row) in lines.iter().enumerate() {
        for j in 0..row.len() {
            // Skip already seen
            if universe_seen.contains(&(i, j)) {
                continue;
            }
            // Create BFS
            let mut stack = vec![(i, j)];
            let mut cur_basin = 0;
            while let Some((cur_i, cur_j)) = stack.pop() {
                if universe_seen.contains(&(cur_i, cur_j)) {
                    continue;
                } else {
                    universe_seen.insert((cur_i, cur_j));
                    cur_basin += 1;
                }
                // Find value
                for (di, dj) in directions.iter() {
                    let (ni, nj) = (cur_i as i32 + di, cur_j as i32 + dj);

                    if ni >= 0 && nj >= 0 && ni < lines.len() as i32 && nj < lines[0].len() as i32 {
                        let coords = (ni as usize, nj as usize);
                        if !universe_seen.contains(&coords) {
                            stack.insert(0, coords);
                        }
                    }
                }
            }
            basins.push(cur_basin);
        }
    }

    basins.sort_by(|a, b| b.cmp(a));
    let p2: i64 = basins.iter().take(3).product();

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
