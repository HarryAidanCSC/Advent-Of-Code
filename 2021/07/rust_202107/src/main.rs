use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").expect("file");
    let lines: Vec<i32> = file
        .trim()
        .split(',')
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    let min_pos: i32 = *lines.iter().min().unwrap();
    let max_pos: i32 = *lines.iter().max().unwrap();
    let mut p1_fuel: i32 = i32::MAX;
    let mut p2_fuel: i32 = i32::MAX;

    for cur_pos in min_pos..=max_pos {
        let mut cur_score1 = 0;
        let mut cur_score2 = 0;
        for pos in &lines {
            cur_score1 += (cur_pos - pos).abs();
            let dist = (cur_pos - pos).abs();
            cur_score2 += dist * (dist + 1) / 2;
        }

        if cur_score1 < p1_fuel {
            p1_fuel = cur_score1;
        }
        if cur_score2 < p2_fuel {
            p2_fuel = cur_score2;
        }
    }

    println!("Part One: {}", p1_fuel);
    println!("Part Two: {}", p2_fuel);
}
