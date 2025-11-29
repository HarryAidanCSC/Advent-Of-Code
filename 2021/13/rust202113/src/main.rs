use std::collections::HashSet;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut coords = HashSet::new();
    let mut p1 = 0;
    for line in lines.iter() {
        if line.is_empty() {
            continue;
        } else if line.starts_with('f') {
            let (_, axis) = line.split_once("=").unwrap();
            let axis = axis.parse::<i32>().unwrap();
            let mut new_coords = coords.clone();

            if line.contains('x') {
                for (x, y) in coords {
                    if x > axis {
                        new_coords.remove(&(x, y));
                        new_coords.insert((2 * axis - x, y));
                    }
                }
            } else if line.contains('y') {
                for (x, y) in coords {
                    if y > axis {
                        new_coords.remove(&(x, y));
                        new_coords.insert((x, 2 * axis - y));
                    }
                }
            }
            coords = new_coords.clone();
            let len = new_coords.len();
            if p1 == 0 {
                p1 = len;
            }
        } else {
            let (x, y) = line.split_once(",").unwrap();
            coords.insert((x.parse::<i32>().unwrap(), y.parse::<i32>().unwrap()));
        }
    }

    // P2
    println!("Part One: {}", p1);
    // println!("Part Two: {}", p2);
    let mut row = vec![' '; 40];
    let mut rows = vec![row.clone(); 7];

    for (x, y) in coords {
        let x = x as usize;
        let y = y as usize;
        rows[y][x] = '|';
    }

    for row in rows {
        let s: String = row.into_iter().collect();
        println!("{:?}", s);
    }
}
