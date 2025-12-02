use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect::<Vec<&str>>()[0].split(',').collect();
    println!("{:?}", lines);

    let mut p1: i64 = 0;
    for line in lines {
        let (start, end) = line.split_once('-').unwrap();
        let start: i64 = start.parse().unwrap();
        let end: i64 = end.parse().unwrap();

        for n in start..=end {
            let n_str: Vec<char> = n.to_string().chars().collect();
            let mut cond = true;
            let (mut left, right) = (0 as usize, n_str.len());
            if right % 2 == 1 {
                continue;
            }
            let mut mid = right / 2;
            while mid < right {
                if n_str[left] != n_str[mid] {
                    cond = false;
                    break;
                }
                left += 1;
                mid += 1;
            }
            if cond {
                p1 += n;
            }
        }
    }
    println!("Part One: {}", p1);
}
