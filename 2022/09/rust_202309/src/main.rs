use std::collections::HashSet;
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<(char, i32)> = file
        .lines()
        .map(|x| x.split_once(' ').unwrap())
        .map(|s| (s.0.chars().next().unwrap(), s.1.parse::<i32>().unwrap()))
        .collect();

    let mut visited = HashSet::from([(0, 0)]);
    let (mut h, mut t) = ((0, 0), (0, 0));

    for (d, n) in lines {
        for _ in 0..n {
            let prev_h = h.clone();
            match d {
                'U' => h.0 += 1,
                'D' => h.0 -= 1,
                'R' => h.1 += 1,
                'L' => h.1 -= 1,
                _ => print!(""),
            }
            if i32::abs(t.0 - h.0) > 1 || i32::abs(t.1 - h.1) > 1 {
                visited.insert(prev_h);
                t = prev_h;
            }
        }
    }

    println!("Part One: {}", visited.len());
}
