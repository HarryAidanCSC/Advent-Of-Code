use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<(i64, i64)> = file
        .lines()
        .map(|line| {
            let s = line.split_once(',').unwrap();
            (s.0.parse::<i64>().unwrap(), s.1.parse::<i64>().unwrap())
        })
        .collect();

    let mut p1 = 0;
    for (x0, y0) in lines.iter() {
        for (x1, y1) in lines.iter() {
            let dx = x1.abs_diff(*x0) + 1;
            let dy = y1.abs_diff(*y0) + 1;
            let area = dx * dy;

            p1 = p1.max(area);
        }
    }
    println!("Part One: {}", p1);
}
