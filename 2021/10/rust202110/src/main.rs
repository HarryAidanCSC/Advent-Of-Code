use std::collections::HashMap;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<char>> = file.lines().map(|l| l.chars().collect()).collect();

    let score_lookup = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);
    let open_close = HashMap::from([(')', '('), (']', '['), ('}', '{'), ('>', '<')]);

    let mut p1 = 0;
    for line in &lines {
        let mut char_stack: Vec<char> = vec![];
        for i in 0..line.len() {
            // peek current position in line stack
            let cur = line[i];
            if !score_lookup.contains_key(&cur) {
                char_stack.push(cur);
            } else {
                // Pop from char stack
                let prev_char = char_stack.pop().unwrap();
                if prev_char != *open_close.get(&cur).unwrap() {
                    p1 += score_lookup.get(&cur).unwrap();
                }
            }
        }
    }

    println!("Part One: {}", p1);
}
