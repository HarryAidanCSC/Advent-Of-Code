use std::collections::HashMap;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../test.txt").unwrap();
    let lines: Vec<Vec<char>> = file.lines().map(|line| line.chars().collect()).collect();
    const DELTAS: [(isize, isize); 8] = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ];
    let mut nbors: HashMap<(isize, isize), i32> = HashMap::new();

    for (j, line) in lines.iter().enumerate() {
        for (i, c) in line.iter().enumerate() {
            if c == &'.' {
                continue;
            }
            for (dj, di) in DELTAS {
                if let Some(row) = lines.get(j.wrapping_add_signed(dj)) {
                    if let Some(&neigh) = row.get(i.wrapping_add_signed(di)) {
                        if neigh == '@' {
                            *nbors.entry((i as isize + di, j as isize + dj)).or_default() += 1;
                        }
                    }
                }
            }
        }
    }

    let mut p1 = 0;
    for value in nbors.values() {
        if value < &4 {
            p1 += 1;
        }
    }
    println!("Part One: {}", p1);
}
