use std::collections::HashMap;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<char>> = file.lines().map(|l| l.chars().collect()).collect();

    let score_lookup = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);
    let close_open = HashMap::from([(')', '('), (']', '['), ('}', '{'), ('>', '<')]);

    let mut incomplete_lines: Vec<Vec<char>> = vec![];
    let mut p1 = 0;
    for line in &lines {
        let mut char_stack: Vec<char> = vec![];
        let mut incomplete = true;
        for i in 0..line.len() {
            // peek current position in line stack
            let cur = line[i];
            if !score_lookup.contains_key(&cur) {
                char_stack.push(cur);
            } else {
                // Pop from char stack
                let prev_char = char_stack.pop().unwrap();
                if prev_char != *close_open.get(&cur).unwrap() {
                    p1 += score_lookup.get(&cur).unwrap();
                    incomplete = false;
                    break;
                }
            }
        }
        if incomplete {
            incomplete_lines.push(line.clone());
        }
    }

    let score_lookup = HashMap::from([('(', 1), ('[', 2), ('{', 3), ('<', 4)]);
    let mut scores: Vec<i64> = vec![];
    for line in &incomplete_lines {
        let mut char_stack: Vec<char> = vec![];
        for i in 0..line.len() {
            let cur = line[i];
            if score_lookup.contains_key(&cur) {
                char_stack.push(cur);
            } else {
                char_stack.pop().unwrap();
            }
        }
        // Go through the stack in reverse
        let mut cur_score: i64 = 0;
        for c in char_stack.iter().rev() {
            cur_score *= 5;
            cur_score += score_lookup.get(&c).unwrap();
        }
        scores.push(cur_score);
    }

    let mid_idx = scores.len() / 2;
    let (_, p2, _) = scores.select_nth_unstable(mid_idx);
    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
