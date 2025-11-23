use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();   
    // 
    let rate_length = lines[0].len();
    let mut bits: Vec<i32> = vec![0; rate_length];

    for line in lines{
        for (i, value) in line.chars().enumerate() {
            if value == '0' {bits[i] += 1;} else {bits[i] -= 1;} 
        }
    }

    let mut gamma = 0;
    let mut epsilon = 0;
    
    for (i, &value) in bits.iter().rev().enumerate(){
        if value > 0 {
            gamma += 1 << i;
        } else {
            epsilon += 1 << i;
        }
    }
    // Part One
    println!("Part One: {}", gamma * epsilon);

}
