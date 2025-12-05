use std::collections::HashSet;
use std::fs;
fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<char> = file.lines().next().unwrap().chars().collect();

    let mut parts = vec![];
    for j in [4, 14] {
        let mut cur = lines[..j].to_vec();

        for i in j..lines.len() {
            cur.remove(0);
            cur.push(lines[i]);
            if cur.len() == cur.iter().collect::<HashSet<_>>().len() {
                parts.push(i + 1);
                break;
            }
        }
    }
    println!("Part One: {}", parts[0]);
    println!("Part One: {}", parts[1]);
}
