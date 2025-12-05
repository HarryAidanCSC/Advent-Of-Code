use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut p1 = 0;
    let mut cycle = 0;
    let mut cur = 1;

    for line in lines {
        if line.starts_with("noop") {
            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                println!("1. {} Cycle: {} Cur {}", cycle * cur, cycle, cur);
                p1 += cycle * cur;
            }
            // Add
        } else {
            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                println!("2. {} Cycle: {} Cur {}", cycle * cur, cycle, cur);
                p1 += cycle * cur;
            }

            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                println!("3. {} Cycle: {} Cur {}", cycle * cur, cycle, cur);
                p1 += cycle * cur;
            }

            let (_, n) = line.split_once(' ').unwrap();
            let n = n.parse::<i32>().unwrap();
            cur += n;
        }
    }
    println!("Part One: {}", p1);
}
