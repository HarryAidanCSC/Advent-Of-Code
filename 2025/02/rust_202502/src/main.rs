use std::collections::HashSet;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect::<Vec<&str>>()[0].split(',').collect();

    let mut p1: i64 = 0;
    let mut p2: i64 = 0;
    for line in lines {
        let (start, end) = line.split_once('-').unwrap();
        let start: i64 = start.parse().unwrap();
        let end: i64 = end.parse().unwrap();
        let mut invalid_ids = HashSet::new();
        for n in start..=end {
            let n_str: String = n.to_string();
            let right = n_str.len();
            let mid = right / 2;

            for i in 1..=mid {
                if right % i != 0 {
                    continue;
                }

                let mut cond = true;
                let ref_str = &n_str[0..i];
                for z in (i..right).step_by(i) {
                    let ns = &n_str[z..z + i];
                    if ns != ref_str {
                        cond = false;
                        break;
                    }
                }

                if cond {
                    invalid_ids.insert(n);
                    if i == mid && right % 2 == 0 {
                        p1 += n;
                    }
                }
            }
        }
        for id in invalid_ids {
            p2 += id;
        }
    }
    println!("Part One: {}", p1);
    println!("Part One: {}", p2);
}
