use std::collections::HashMap;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
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
    let mut nbors: HashMap<(usize, usize), i32> = HashMap::new();

    for (j, line) in lines.iter().enumerate() {
        for (i, c) in line.iter().enumerate() {
            if c == &'.' {
                continue;
            }
            for (dj, di) in DELTAS {
                let (jindex, index) = (j.wrapping_add_signed(dj), i.wrapping_add_signed(di));
                if let Some(row) = lines.get(jindex) {
                    if let Some(&neigh) = row.get(index) {
                        if neigh == '@' {
                            *nbors.entry((jindex, index)).or_default() += 1;
                        }
                    }
                }
            }
            nbors.entry((j, i)).or_insert(0);
        }
    }

    let mut p1 = 0;
    for value in nbors.values() {
        if value < &4 {
            p1 += 1;
        }
    }

    // P2
    let mut p2 = 0;
    loop {
        let mut new_nbors: HashMap<(usize, usize), i32> = HashMap::new();
        let mut to_remove = vec![];
        for (key, val) in &nbors {
            if val < &4 {
                to_remove.push(key);
                p2 += 1;
            } else {
                new_nbors.insert(*key, *val);
            }
        }

        if to_remove.len() == 0 {
            break;
        }

        // Update nbors
        for (j, i) in to_remove {
            for (dj, di) in DELTAS {
                let key = (j.wrapping_add_signed(dj), i.wrapping_add_signed(di));
                new_nbors.entry(key).and_modify(|cnt| *cnt -= 1);
            }
        }
        nbors = new_nbors;
    }

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
