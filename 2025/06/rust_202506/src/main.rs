use std::collections::HashMap;
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut nums: HashMap<usize, Vec<i64>> = HashMap::new();
    let mut operands = vec![];

    for line in lines {
        for (i, s) in line.split_whitespace().enumerate() {
            if ["*", "+"].contains(&s) {
                operands.push(s);
            } else {
                let num = s.parse::<i64>().unwrap();
                nums.entry(i).or_default().push(num);
            }
        }
    }

    // P1
    let mut p1: i64 = 0;
    for (key, value) in nums {
        let operand = operands[key];
        p1 += match operand {
            "*" => value.iter().product(),
            "+" => value.iter().sum(),
            _ => 0,
        };
    }

    println!("Part One: {}", p1);
}
