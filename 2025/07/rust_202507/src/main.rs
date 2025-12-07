use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<char>> = file.lines().map(|x| x.chars().collect()).collect();
    let maxy = lines.len() - 1;
    let maxx = lines[0].len() - 1;
    // Starting Position
    let start: (usize, usize) = (
        0,
        lines[0]
            .iter()
            .enumerate()
            .filter_map(|(i, x)| if x == &'S' { Some(i) } else { None })
            .nth(0)
            .unwrap(),
    );

    let mut heap = BinaryHeap::new();
    heap.push(Reverse(start));

    // Splitter locations
    let splitters: HashSet<(usize, usize)> = lines
        .iter()
        .enumerate()
        .flat_map(|(j, y)| {
            y.iter()
                .enumerate()
                .filter_map(|(i, x)| if x == &'^' { Some(i) } else { None })
                .map(move |coord| (j, coord))
        })
        .collect();

    let mut p1 = HashSet::new();
    let mut p2 = 0;
    let mut visited: HashMap<(usize, usize), i64> = HashMap::new();
    visited.insert(start, 1);
    while let Some(Reverse((mut y, x))) = heap.pop() {
        // Increase y until next splitter found
        let cur_n = *visited.get(&(y, x)).unwrap();
        y += 1;

        while y < maxy {
            if splitters.contains(&(y, x)) {
                p1.insert((y, x));
                if x > 0 {
                    if !visited.contains_key(&(y, x - 1)) {
                        heap.push(Reverse((y, x - 1)));
                    }
                    *visited.entry((y, x - 1)).or_insert(0) += cur_n;
                }
                if x < maxx {
                    if !visited.contains_key(&(y, x + 1)) {
                        heap.push(Reverse((y, x + 1)));
                    }
                    *visited.entry((y, x + 1)).or_insert(0) += cur_n;
                }

                break;
            } else {
                y += 1;
            }
        }
        if y == maxy {
            p2 += cur_n;
        }
    }
    println!("Part One: {}", p1.len());
    println!("Part Two: {}", p2);
}
