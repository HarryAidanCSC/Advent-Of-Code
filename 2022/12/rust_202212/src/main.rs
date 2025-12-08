use std::collections::{HashMap, VecDeque};
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let mut lines: Vec<Vec<u8>> = file
        .lines()
        .map(|x| x.chars().map(|c| c as u8).collect())
        .collect();

    let (mut start, mut end) = ((0, 0, 97 as u8, 0 as usize), (0, 0));
    let mut p2_start = VecDeque::new();
    let mut best2 = HashMap::new();
    for (j, line) in lines.iter().enumerate() {
        for (i, val) in line.iter().enumerate() {
            if val == &69 {
                end = (j, i);
            } else if val == &83 {
                start = (j, i, 97, 0);
            } else if val == &97 {
                p2_start.push_front((j, i, 97, 0));
                best2.insert((j, i), 0);
            }
        }
    }

    lines[start.0 as usize][start.1 as usize] = 97;
    lines[end.0 as usize][end.1 as usize] = 122;

    let mut queue = VecDeque::from([start.clone()]);
    const DELTAS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    let mut p1 = 0;
    let mut best: HashMap<(usize, usize), usize> = HashMap::from([((start.0, start.1), 1)]);

    'beef: while let Some((y, x, cur, visit_n)) = queue.pop_front() {
        if best.get(&(y, x)).unwrap() < &visit_n {
            continue;
        }
        // Neighbours
        for (dy, dx) in DELTAS {
            let (ny, nx) = (y as i32 + dy, x as i32 + dx);

            if let Some(&v) = lines.get(ny as usize).and_then(|row| row.get(nx as usize)) {
                let (ny, nx) = (ny as usize, nx as usize);
                if best.contains_key(&(ny, nx)) && *best.get(&(ny, nx)).unwrap() <= visit_n + 1 {
                    continue;
                } else {
                    if v <= cur + 1 {
                        // END condition
                        if (ny, nx) == end {
                            p1 = visit_n + 1;
                            break 'beef;
                        }
                        queue.push_back((ny, nx, v, visit_n + 1));
                        best.insert((ny, nx), visit_n + 1);
                    }
                }
            }
        }
    }

    // P2
    let mut p2 = 0;
    'pork: while let Some((y, x, cur, visit_n)) = p2_start.pop_front() {
        if best.get(&(y, x)).unwrap() < &visit_n {
            continue;
        }
        // Neighbours
        for (dy, dx) in DELTAS {
            let (ny, nx) = (y as i32 + dy, x as i32 + dx);

            if let Some(&v) = lines.get(ny as usize).and_then(|row| row.get(nx as usize)) {
                let (ny, nx) = (ny as usize, nx as usize);
                if best2.contains_key(&(ny, nx)) && *best2.get(&(ny, nx)).unwrap() <= visit_n + 1 {
                    continue;
                } else {
                    if v <= cur + 1 {
                        // END condition
                        if (ny, nx) == end {
                            p2 = visit_n + 1;
                            break 'pork;
                        }
                        p2_start.push_back((ny, nx, v, visit_n + 1));
                        best2.insert((ny, nx), visit_n + 1);
                    }
                }
            }
        }
    }
    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
