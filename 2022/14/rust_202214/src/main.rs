use std::collections::HashSet;
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<(usize, usize)>> = file
        .lines()
        .map(|line| {
            line.split(" -> ")
                .map(|c| {
                    let (x, y) = c.split_once(',').unwrap();
                    (x.parse::<usize>().unwrap(), y.parse::<usize>().unwrap())
                })
                .collect()
        })
        .collect();

    let mut maxy = 0;
    // Occupado
    let mut occupado: HashSet<(usize, usize)> = HashSet::new();
    for line in lines {
        let (mut x, mut y) = (line[0].0, line[0].1);
        maxy = maxy.max(y);
        for coords in &line[1..] {
            for dx in x.min(coords.0)..=x.max(coords.0) {
                for dy in y.min(coords.1)..=y.max(coords.1) {
                    occupado.insert((dx, dy));
                }
            }
            x = coords.0;
            y = coords.1;
            maxy = maxy.max(y);
        }
    }

    // Kick off
    let mut occupada = occupado.clone();
    let mut p1 = 0;
    loop {
        p1 += 1;
        let (mut x, mut y) = (500, 0);
        // Drop the y
        while y <= maxy {
            y += 1;
            if !occupado.contains(&(x, y)) {
            } else if !occupado.contains(&(x - 1, y)) {
                x -= 1;
            } else if !occupado.contains(&(x + 1, y)) {
                x += 1;
            } else {
                occupado.insert((x, y - 1));
                y -= 1;
                break;
            }
        }
        if y == maxy + 1 {
            break;
        }
    }

    // P2
    let abs_max = maxy + 2;
    let mut i = 0;
    let mut p2 = 0;
    loop {
        i += 1;

        let (mut x, mut y) = (500, 0);
        // Drop the y
        while y <= abs_max {
            y += 1;
            if y < abs_max && !occupada.contains(&(x, y)) {
            } else if y < abs_max && !occupada.contains(&(x - 1, y)) {
                x -= 1;
            } else if y < abs_max && !occupada.contains(&(x + 1, y)) {
                x += 1;
            } else {
                occupada.insert((x, y - 1));
                y -= 1;
                break;
            }
        }
        if y == 0 {
            p2 = i;
            break;
        }
    }
    println!("Part One: {}", p1 - 1);
    println!("Part Two: {}", p2);
}
