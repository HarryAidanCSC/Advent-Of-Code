use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

fn sort_token(s: &str) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort();
    chars.into_iter().collect()
}

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let unique_lengths: HashSet<usize> = HashSet::from([2, 4, 3, 7]);

    let mut p1 = 0;
    let mut p2 = 0;
    for line in &lines {
        let (input, output) = line.split_once(" | ").unwrap();
        let output_members: Vec<&str> = output.split_whitespace().collect();
        for member in &output_members {
            if unique_lengths.contains(&member.len()) {
                p1 += 1;
            }
        }

        // Part Two
        let input_members: Vec<&str> = input.split_whitespace().collect();
        let mut known: HashMap<i32, Vec<char>> = HashMap::new();
        let mut unknown: HashMap<i32, Vec<String>> = HashMap::new();
        let mut answers: HashMap<String, i32> = HashMap::new();

        for m in input_members.iter() {
            let length: i32 = m.len() as i32;
            if unique_lengths.contains(&m.len()) {
                let chars: Vec<char> = m.chars().collect();
                known.insert(length, chars);
                let m_key = sort_token(m);
                match length {
                    2 => {
                        answers.insert(m_key.to_string(), 1);
                    }
                    3 => {
                        answers.insert(m_key.to_string(), 7);
                    }
                    4 => {
                        answers.insert(m_key.to_string(), 4);
                    }
                    7 => {
                        answers.insert(m_key.to_string(), 8);
                    }
                    _ => {}
                }
            } else {
                unknown.entry(length).or_default().push(m.to_string());
            }
        }

        ///// Find 9

        let four = known.get(&4).unwrap();
        let char0 = four[0];
        let char1 = four[1];
        let char2 = four[2];
        let char3 = four[3];
        for word in unknown.get(&6).unwrap() {
            let chars: Vec<char> = word.chars().collect();
            if chars.contains(&char0)
                && chars.contains(&char1)
                && chars.contains(&char2)
                && chars.contains(&char3)
            {
                let m_key = sort_token(word);
                answers.insert(m_key, 9);
            }
        }

        // Find 0
        let one = known.get(&2).unwrap();
        let char0 = one[0];
        let char1 = one[1];
        for word in unknown.get(&6).unwrap() {
            let m_key = sort_token(word);
            if answers.contains_key(&m_key) {
                continue;
            }
            let chars: Vec<char> = word.chars().collect();
            if chars.contains(&char0) && chars.contains(&char1) {
                answers.insert(m_key, 0);
            }
        }

        // Find 6
        let mut sixer_my_goodness: Vec<char> = vec![];
        for word in unknown.get(&6).unwrap() {
            let m_key = sort_token(word);
            if answers.contains_key(&m_key) {
                continue;
            } else {
                answers.insert(m_key, 6);
                let chars: Vec<char> = word.chars().collect();
                sixer_my_goodness = chars.clone();
                break;
            }
        }

        // Find 3
        for word in unknown.get(&5).unwrap() {
            let chars: Vec<char> = word.chars().collect();
            if chars.contains(&char0) && chars.contains(&char1) {
                let m_key = sort_token(word);
                answers.insert(m_key, 3);
            }
        }

        // Find 5
        for word in unknown.get(&5).unwrap() {
            let m_key = sort_token(word);
            if answers.contains_key(&m_key) {
                continue;
            }
            let chars: Vec<char> = word.chars().collect();

            let mut cond = true;
            for char in &chars {
                if !sixer_my_goodness.contains(&char) {
                    cond = false;
                    break;
                }
            }

            if cond {
                answers.insert(m_key, 5);
                break;
            }
        }

        // Find 2
        for word in unknown.get(&5).unwrap() {
            let m_key = sort_token(word);
            if answers.contains_key(&m_key) {
                continue;
            } else {
                answers.insert(m_key, 2);
                break;
            }
        }

        let mut cur_score = 0;
        let mut f = 1000;
        for word in output_members {
            let m_key = sort_token(word);
            let value = f * answers.get(&m_key).unwrap();
            cur_score += value;
            f /= 10;
        }
        p2 += cur_score
        // break;
    }
    println!("Part One {}", p1);
    println!("Part Two {}", p2);
}
