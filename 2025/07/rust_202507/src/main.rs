use std::collections::{HashSet, VecDeque};
use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<char>> = file.lines().map(|x| x.chars().collect()).collect();
    let maxy = lines.len() - 1;
    let maxx = lines[0].len() - 1;
    // Starting Position
    let start: (usize, usize) = (
        lines[0]
            .iter()
            .enumerate()
            .filter_map(|(i, x)| if x == &'S' { Some(i) } else { None })
            .nth(0)
            .unwrap(),
        0,
    );

    let mut queue = VecDeque::from([start]);

    // Splitter locations
    let splitters: HashSet<(usize, usize)> = lines
        .iter()
        .enumerate()
        .flat_map(|(j, y)| {
            y.iter()
                .enumerate()
                .filter_map(|(i, x)| if x == &'^' { Some(i) } else { None })
                .map(move |coord| (coord, j))
        })
        .collect();

    let mut p1 = HashSet::new();
    let mut seen = HashSet::new();
    while let Some((x, mut y)) = queue.pop_back() {
        // Increase y until next splitter found
        y += 1;
        if seen.contains(&(x, y)) {
            continue;
        }
        seen.insert((x, y));
        while y <= maxy {
            if splitters.contains(&(x, y)) {
                p1.insert((x, y));
                if x > 0 {
                    queue.push_front((x - 1, y));
                }
                if x < maxx {
                    queue.push_front((x + 1, y));
                }
                break;
            } else {
                y += 1;
            }
        }
    }

    println!("Part One: {}", p1.len());
}
