use std::fs;
fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i32>> = file
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap() as i32)
                .collect()
        })
        .collect();

    // Part one
    let mut p1 = 0;
    for line in &lines {
        let mut cur_max = 0;

        for (i, v0) in line[..line.len() - 1].iter().enumerate() {
            let mut cur = 10 * v0;
            let max_val = *line[i + 1..].iter().max().unwrap();
            cur += max_val;
            cur_max = cur_max.max(cur);
        }
        p1 += cur_max;
    }
    // println!("{:?}", lines);
    println!("Part One: {}", p1);
}
