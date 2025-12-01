use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();
    let mut p1 = 50;
    let mut p1_score = 0;

    for line in lines {
        let mut num = line[1..].parse::<i32>().unwrap() % 100;
        if line.contains('L') {
            num *= -1;
        }
        p1 += num;

        if p1 < 0 {
            p1 -= 100;
            p1 %= 100;
            p1 += 100;
        } else if p1 >= 100 {
            p1 %= 100;
        }

        if p1 == 0 {
            p1_score += 1;
        }
    }

    println!("Part One : {}", p1_score);
}
