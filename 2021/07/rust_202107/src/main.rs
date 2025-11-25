use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").expect("file");
    let lines: Vec<i32> = file
        .split(',')
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    let min_pos: i32 = *lines.iter().min().unwrap();
    let max_pos: i32 = *lines.iter().max().unwrap();
    let mut min_fuel: i32 = i32::MAX;

    for cur_pos in min_pos - 100..=max_pos + 100 {
        let mut cur_score = 0;
        for pos in &lines {
            cur_score += (cur_pos - pos).abs()
        }

        if cur_score < min_fuel {
            min_fuel = cur_score;
        }
    }

    println!("Part One: {}", min_fuel);
}
