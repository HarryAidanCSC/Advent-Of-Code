use std::fs;
use std::collections::HashMap;
use std::cmp::{min, max};

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect(); 

    let mut coords: HashMap<(i32, i32), i32> = HashMap::new();
    let mut coordsp2: HashMap<(i32, i32), i32> = HashMap::new();

    let mut p1 = 0;
    let mut p2 = 0;
    for line in &lines{
        let split_line: Vec<i32> = line
            .split(" -> ")
            .flat_map(|s| s.split(","))
            .map(|s| s.parse().unwrap())
            .collect();

        let minx = min(split_line[0], split_line[2]);
        let maxx = max(split_line[0], split_line[2]);
        let miny = min(split_line[1], split_line[3]);
        let maxy = max(split_line[1], split_line[3]);

        if (minx != maxx) && (miny != maxy){
            let mut i = 0;
            let (x, y, x1) = (split_line[0], split_line[1], split_line[2]);
            let x_dir = if x == minx { 1 } else { -1 };
            let y_dir = if y == miny { 1 } else { -1 };
            while x + ((i-1)*x_dir) != x1 {
                let count = coordsp2.entry((x + (i * x_dir), y + (i * y_dir))).or_insert(0);
                *count += 1;
                if *count == 2 {
                    p2 += 1;
                }
                i += 1;
            }
        } else {
        // Iterate through the line
        for x in minx..=maxx{
            for y in miny..=maxy{
                // P1
                let count = coords.entry((x,y)).or_insert(0);
                *count += 1;
                if *count == 2 {
                    p1 += 1;
                }
                // P2
                let count = coordsp2.entry((x,y)).or_insert(0);
                *count += 1;
                if *count == 2 {
                    p2 += 1;
                }
            }
            }
        }
        
    }
    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}