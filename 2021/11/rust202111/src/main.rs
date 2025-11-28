use std::collections::VecDeque;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i32>> = file
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
        .collect();

    let mut p1 = 0;
    let mut mlines = lines.clone();
    let octopi = (lines.len() as i32) * (lines[0].len() as i32);
    for i in 0..2500 {
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        let mut octopussy = 0;

        // Add energy to every octopus and keep track of flashing ones
        for (i, row) in mlines.iter_mut().enumerate() {
            for (j, value) in row.iter_mut().enumerate() {
                *value += 1;
                *value %= 10;
                if value == &0 {
                    queue.push_front((i, j));
                }
            }
        }

        // Flash the octopi
        while let Some((cur_i, cur_j)) = queue.pop_back() {
            octopussy += 1;

            // Update neighbours
            for di in -1..=1 {
                for dj in -1..=1 {
                    if !(di == 0 && dj == 0) {
                        let (ni, nj) = ((cur_i as i32 + di) as usize, (cur_j as i32 + dj) as usize);

                        if let Some(neighbour) =
                            mlines.get_mut(ni as usize).and_then(|r| r.get_mut(nj))
                        {
                            if neighbour == &0 {
                                continue;
                            }
                            *neighbour += 1;
                            *neighbour %= 10;
                            if neighbour == &0 {
                                queue.push_front((ni, nj));
                            }
                        }
                    }
                }
            }
        }

        p1 += octopussy;
        if i == 99 {
            println!("Part One: {}", p1);
        }
        if octopussy == octopi {
            println!("Part Two {}", i + 1);
            break;
        }
    }
}
