use std::fs;
fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut ranges = vec![];
    let mut nums = vec![];

    let mut cond = true;
    for line in lines.iter() {
        if line.len() == 0 {
            cond = false;
            continue;
        }

        if cond {
            let range: (i64, i64) = line
                .split_once('-')
                .map(|(a, b)| (a.parse().unwrap(), b.parse().unwrap()))
                .unwrap();
            ranges.push(range);
        } else {
            let val: i64 = line.parse().unwrap();
            nums.push(val);
        }
    }

    let mut p1 = 0;
    for n in nums {
        let mut fresh = false;
        for (key, value) in &ranges {
            if &n >= key && &n <= value {
                fresh = true;
                break;
            }
        }
        if fresh {
            p1 += 1;
        }
    }

    // P2
    ranges.sort();
    let mut cend = -1;
    let mut p2 = 0;
    for (start, end) in ranges {
        let es = start.max(cend + 1);
        if end >= es {
            p2 += end - es + 1;
            cend = end.max(cend);
        }
    }

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
