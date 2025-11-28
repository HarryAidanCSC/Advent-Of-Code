use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i32>> = file
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
        .collect();

    // Part One
    let mut p1 = 0;
    let directions = [(0, 1), (1, 0), (-1, 0), (0, -1)];

    for (i, row) in lines.iter().enumerate() {
        for (j, value) in row.iter().enumerate() {
            let mut skip = false;

            for (di, dj) in directions.iter() {
                let (ni, nj) = (i as i32 + di, j as i32 + dj);
                if let Some(neighbour) = lines.get(ni as usize).and_then(|r| r.get(nj as usize)) {
                    if neighbour <= value {
                        skip = true;
                        break;
                    }
                }
            }
            if !skip {
                p1 += 1 + value;
            }
        }
    }

    println!("Part One: {}", p1);
}
