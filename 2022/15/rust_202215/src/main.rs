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
    let mut p2_lines: Vec<(i32, i32, i32)> = vec![];
    let mut p1: HashSet<i32> = HashSet::new();
    for (x0, y0, x1, y1) in lines {
        let w = x0.max(x1) - x0.min(x1);
        let h = y0.max(y1) - y0.min(y1);
        let mh = w + h;

        let gap = mh - y0.abs_diff(2000000) as i32;
        if gap >= 0 {
            for i in 0..=gap {
                p1.insert(x0 - i);
                p1.insert(x0 + i);
            }
        }
        p2_lines.push((x0, y0, mh));
    }

    p1.retain(|x| !beacons.contains(&(*x, 2000000)));
    println!("{:?}", p2_lines);
    // P2
    let mut p2: i64 = 0;
    'beef: for row in 0..4_000_000 {
        let mut ranges = vec![];

        for (x, y, mh) in p2_lines.iter() {
            let gap = mh - y.abs_diff(row) as i32;
            if gap >= 0 {
                ranges.push((x - gap, x + gap));
            }
        }

        ranges.sort();
        let mut cur_max = ranges[0].1;

        for (start, end) in ranges[1..].iter() {
            if *start > cur_max + 1 {
                p2 = ((cur_max as i64 + 1) * 4_000_000) + row as i64;
                break 'beef;
            }
            cur_max = cur_max.max(*end);
        }
    }

    println!("Part One: {}", p1.len());
    println!("Part Two: {}", p2)
}
