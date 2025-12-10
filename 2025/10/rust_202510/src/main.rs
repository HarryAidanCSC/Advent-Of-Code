use std::collections::VecDeque;
use std::fs::read_to_string;
use std::iter::zip;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    //
    let configs: Vec<Vec<usize>> = lines
        .iter()
        .map(|line| {
            line.split_once(' ')
                .unwrap()
                .0
                .chars()
                .filter(|&c| c == '#' || c == '.')
                .map(|c| if c == '#' { 1 } else { 0 })
                .collect()
        })
        .collect();

    //
    let mut options = vec![];
    for line in lines {
        let mut line_vec = vec![];
        for part in line.split_whitespace() {
            let mut v = vec![];
            if part.starts_with('(') {
                for c in part[1..part.len() - 1].split(',') {
                    v.push(c.parse::<usize>().unwrap());
                }
                line_vec.push(v);
            }
        }
        options.push(line_vec);
    }

    let mut p1 = 0;
    for (config, option) in zip(configs, options.clone()) {
        let start = vec![0; config.len()];
        let mut queue = VecDeque::from([(start, 0)]);

        // BFS
        'beef: while let Some((conf, score)) = queue.pop_front() {
            // Neigbours
            for buttons in option.iter() {
                let mut new_conf = conf.clone();
                for button in buttons {
                    new_conf[*button] ^= 1;
                }

                if new_conf == config {
                    p1 += score + 1;
                    break 'beef;
                } else {
                    queue.push_back((new_conf, score + 1));
                }
            }
        }
    }

    println!("Part One: {}", p1);
}
