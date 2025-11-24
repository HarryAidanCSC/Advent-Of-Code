use std::fs;
use std::collections::HashMap;
use std::cmp::{min, max};

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect(); 

    let mut coords: HashMap<(i32, i32), i32> = HashMap::new();
    let mut p1 = 0;
    for line in &lines{
        let split_line: Vec<i32> = line
            .split(" -> ")
            .flat_map(|s| s.split(","))
            .map(|s| s.parse().unwrap())
            .collect();


        if (split_line[0] != split_line[2]) && (split_line[1] != split_line[3]){
            continue;
        } else {
            println!("{:?}", split_line);
        }
        // Iterate through the line
        for x in min(split_line[0], split_line[2])..=max(split_line[0], split_line[2]){
            for y in min(split_line[1], split_line[3])..=max(split_line[1], split_line[3]){
                let count = coords.entry((x,y)).or_insert(0);
                *count += 1;
                if *count == 2 {
                    p1 += 1;
                }
            }
        }
        
    }
    println!("{:?}", coords);
    println!("Part One: {}", p1);
}