use std::collections::HashSet;
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<(char, i32)> = file
        .lines()
        .map(|x| x.split_once(' ').unwrap())
        .map(|s| (s.0.chars().next().unwrap(), s.1.parse::<i32>().unwrap()))
        .collect();

    // P1
    let mut visited0 = HashSet::from([(0, 0)]);
    let mut visited1 = HashSet::from([(0, 0)]);
    let mut h = (0, 0);
    let mut ts = [(0, 0); 9];

    for (d, n) in lines {
        for _ in 0..n {
            match d {
                'U' => h.1 += 1,
                'D' => h.1 -= 1,
                'R' => h.0 += 1,
                'L' => h.0 -= 1,
                _ => print!(""),
            }

            let mut nts = [(0, 0); 9];
            let mut p = h;
            for (i, t) in ts.iter().enumerate() {
                let (xdiff, ydiff): (i32, i32) = (p.0 - t.0, p.1 - t.1);

                // X
                let mut dx = 0;
                if xdiff < 0 {
                    dx = -1;
                } else if xdiff > 0 {
                    dx = 1;
                }

                // Y
                let mut dy = 0;
                if ydiff < 0 {
                    dy = -1;
                } else if ydiff > 0 {
                    dy = 1;
                }

                let mut newt = *t;
                if xdiff.abs() + ydiff.abs() >= 3 {
                    newt = (newt.0 + dx, newt.1 + dy);
                } else if xdiff.abs() == 2 && ydiff.abs() == 0 {
                    newt = (newt.0 + dx, newt.1);
                } else if xdiff.abs() == 0 && ydiff.abs() == 2 {
                    newt = (newt.0, newt.1 + dy);
                } else {
                    newt = (newt.0, newt.1);
                }

                nts[i] = newt;
                p = newt;
            }

            ts = nts;
            visited0.insert(ts[0]);
            visited1.insert(ts[8]);
        }
    }

    // P2

    println!("Part One: {}", visited0.len());
    println!("Part Two: {}", visited1.len());
}
