use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();   
    // 
    let rate_length = lines[0].len();
    let mut bits: Vec<i32> = vec![0; rate_length];

    for line in &lines{
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

    // Part Two 
    let mut part_two = 1;
    for rate_type in 0..2{

        let mut oxy = lines.clone();

        for i in 0..rate_length {
            if oxy.len() == 1 {break}

            let mut new_oxy: Vec<Vec<&str>> = vec![vec![]; 2];


            for value in oxy.iter(){
                if value.chars().nth(i).unwrap() == '1' {
                    new_oxy[1].push(value)
                } else {
                    new_oxy[0].push(value)
                }
            }
            
            let zs = new_oxy[0].len();
            let os = new_oxy[1].len();
            if rate_type == 0 {
                if os >= zs { oxy = new_oxy[1].clone(); }
                else { oxy = new_oxy[0].clone(); }
            } else {
                if zs <= os { oxy = new_oxy[0].clone(); }
                else { oxy = new_oxy[1].clone(); }
            };

        }
        part_two *= i32::from_str_radix(oxy[0], 2).unwrap();
    }

    println!("Part One: {}", gamma * epsilon);
    println!("Part Two: {}", part_two);
}
