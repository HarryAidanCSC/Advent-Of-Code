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

    let mut p2: i64 = 0;
    for mut line in lines {
        let mut to_remove = line.len() - 12;
        let mut i = 0;

        while to_remove > 0 && i < line.len() {
            let end_limit = (i + to_remove + 1).min(line.len());

            let max_val = line[i..end_limit].iter().copied().max().unwrap_or(0);

            let relative_idx = line[i..end_limit]
                .iter()
                .position(|&x| x == max_val)
                .unwrap();
            let absolute_idx = i + relative_idx;

            for k in i..absolute_idx {
                line[k] = 0;
                to_remove -= 1;
            }

            i = absolute_idx + 1;
        }

        let mut cur: i64 = 0;
        let mut f: i64 = 1;
        line.retain(|&x| x != 0);
        for val in line[..12].iter().rev() {
            cur += f * *val as i64;
            f *= 10;
        }
        println!("{:?}", cur);
        p2 += cur;
    }
    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
