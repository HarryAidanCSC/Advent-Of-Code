use std::collections::HashMap;
use std::fs::read_to_string;
use std::iter::once;

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut nums0: HashMap<usize, Vec<i64>> = HashMap::new();
    let mut nums1: HashMap<usize, HashMap<usize, Vec<char>>> = HashMap::new();

    let splits: Vec<usize> = lines[lines.len() - 1]
        .chars()
        .enumerate()
        .filter_map(|(i, x)| if x != ' ' { Some(i) } else { None })
        .chain(once(lines[0].len()))
        .collect();

    let operands: Vec<&str> = lines[lines.len() - 1].split_whitespace().collect();

    for line in lines {
        let mut prev = splits[0];

        for (i, split) in splits[1..].iter().enumerate() {
            if let Some(s) = line.get(prev..*split) {
                if !s.contains(&['+', '*'][..]) {
                    let num = s.trim().parse::<i64>().unwrap();
                    nums0.entry(i).or_default().push(num);

                    for (idx, c) in s.chars().enumerate() {
                        if c == ' ' {
                            continue;
                        }
                        nums1.entry(i).or_default().entry(idx).or_default().push(c);
                    }
                }
            }
            prev = *split;
        }
    }

    // P1
    let p1: i64 = nums0
        .iter()
        .map(|(key, value)| match operands[*key] {
            "*" => value.iter().product(),
            "+" => value.iter().sum(),
            _ => 0,
        })
        .sum();

    // P2
    let mut p2: i64 = 0;
    for (key, value) in &nums1 {
        let operand = operands[*key];
        let mut cur = match operand {
            "*" => 1,
            _ => 0,
        };
        for (_, values) in value {
            let s: String = values.iter().collect();
            let n = s.parse::<i64>().unwrap();
            match operand {
                "*" => {
                    cur *= n;
                }
                "+" => {
                    cur += n;
                }
                _ => {}
            }
        }
        p2 += cur;
    }
    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
