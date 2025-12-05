use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut p1 = 0;
    let mut cycle: i32 = 0;
    let mut cur: i32 = 1;
    let mut render: [[char; 40]; 6] = [['.'; 40]; 6];

    for line in lines {
        // P2
        let pos = cycle % 40;
        println!("Pos {}  Reg {}", pos, cur);
        if cur >= pos - 1 && cur < (pos + 2) {
            render[(cycle / 40) as usize][pos as usize] = '#';
        }

        if line.starts_with("noop") {
            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                p1 += cycle * cur;
            }
        } else {
            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                p1 += cycle * cur;
            }

            // P2
            let pos = cycle % 40;

            if cur >= pos - 1 && cur < (pos + 2) {
                render[(cycle / 40) as usize][pos as usize] = '#';
            }
            //
            cycle += 1;
            if (cycle + 20) % 40 == 0 {
                p1 += cycle * cur;
            }

            let (_, n) = line.split_once(' ').unwrap();
            let n = n.parse::<i32>().unwrap();
            cur += n;
        }
    }
    println!("Part One: {}", p1);
    for line in render {
        let render_line: String = line.iter().collect();
        println!("{}", render_line)
    }
}
