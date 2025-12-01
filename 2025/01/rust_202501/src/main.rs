use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();
    let mut p1 = 0;
    let mut p2 = 0;
    let mut cur_score = 50;

    for line in lines {
        let numero = line[1..].parse::<i32>().unwrap();
        let num = if line.contains('L') { -1 } else { 1 };

        for _ in 0..numero {
            cur_score += num;
            if cur_score == -1 {
                cur_score = 99;
            } else if cur_score == 100 {
                cur_score = 0;
            }

            if cur_score == 0 {
                p2 += 1;
            }
        }

        if cur_score == 0 {
            p1 += 1;
        }
    }

    println!("Part One : {}", p1);
    println!("Part Two : {}", p2);
}
