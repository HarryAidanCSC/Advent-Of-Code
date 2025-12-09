use std::collections::HashSet;
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<(i32, i32, i32, i32)> = file
        .lines()
        .map(|l| {
            let nums: Vec<i32> = l
                .split(|c: char| !c.is_numeric() && c != '-')
                .filter(|s| !s.is_empty())
                .map(|s| s.parse().unwrap())
                .collect();
            (nums[0], nums[1], nums[2], nums[3])
        })
        .collect();

    let beacons: HashSet<(i32, i32)> = lines.iter().map(|c| (c.2, c.3)).collect();

    let mut p1: HashSet<i32> = HashSet::new();
    for (x0, y0, x1, y1) in lines {
        let w = x0.max(x1) - x0.min(x1);
        let h = y0.max(y1) - y0.min(y1);
        let mh = w + h;

        let gap = mh - y0.abs_diff(2000000) as i32;
        if x0 == 8 && y0 == 7 {
            println!("{}", mh);
        }
        if gap >= 0 {
            for i in 0..=gap {
                p1.insert(x0 - i);
                p1.insert(x0 + i);
            }
        }
    }

    p1.retain(|x| !beacons.contains(&(*x, 2000000)));
    println!("Part One: {}", p1.len());
}
