use std::collections::HashSet;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let unique_lengths: HashSet<usize> = HashSet::from([2, 4, 3, 7]);

    let mut p1 = 0;
    for line in lines {
        let (_, output) = line.split_once(" | ").unwrap();
        let output_members: Vec<&str> = output.split_whitespace().collect();
        for member in output_members {
            if unique_lengths.contains(&member.len()) {
                p1 += 1;
            }
        }
    }

    println!("Part One: {}", p1);
}
