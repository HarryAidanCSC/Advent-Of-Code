use std::collections::HashSet;
use std::fs;
fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<char> = file.lines().next().unwrap().chars().collect();

    let mut cur = lines[..4].to_vec();
    let mut p1 = 0;

    for i in 4..lines.len() {
        cur.remove(0);
        cur.push(lines[i]);
        if cur.len() == cur.iter().collect::<HashSet<_>>().len() {
            p1 = i + 1;
            break;
        }
    }

    println!("Part One: {}", p1);
}
