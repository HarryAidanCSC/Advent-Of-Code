use std::{fs, sync::Mutex};

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();
    
    let mut timers: Vec<i64> = vec![0; 9];
    for val in lines[0].split(","){
        let timer: usize = val.parse().expect("Not a number");
        timers[timer] += 1;

    }

    // Simulation
    for _ in 0..80{
        let zero_lifers = timers.remove(0);
        timers[6] += zero_lifers;
        timers.push(zero_lifers);
    }
    
    println!("Part One: {:?}", timers.iter().sum::<i64>());
}