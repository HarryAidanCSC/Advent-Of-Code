use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
use std::fs;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let mut nodes: HashMap<String, Vec<String>> = HashMap::new();
    let mut queue: VecDeque<(String, HashSet<String>)> = VecDeque::from([(
        String::from("start"),
        HashSet::from([String::from("start")]),
    )]);

    for line in lines.iter() {
        let (a, b) = line.split_once("-").unwrap();
        nodes.entry(a.to_string()).or_default().push(b.to_string());
        nodes.entry(b.to_string()).or_default().push(a.to_string());
    }
    // P1
    let mut p1 = 0;
    while let Some((cur_node, path)) = queue.pop_front() {
        for nb in nodes.get(&cur_node).unwrap().iter() {
            if nb == "end" {
                p1 += 1;
            } else if !path.contains(nb) {
                let mut new_path = path.clone();
                if !nb.chars().any(|c| c.is_uppercase()) {
                    new_path.insert(nb.to_string());
                }
                queue.push_back((nb.to_string(), new_path));
            }
        }
    }

    // P2
    let mut p2 = 0;
    let mut queue: VecDeque<(String, HashSet<String>, bool)> =
        VecDeque::from([(String::from("start"), HashSet::new(), true)]);
    while let Some((cur_node, path, cond)) = queue.pop_front() {
        for nb in nodes.get(&cur_node).unwrap().iter() {
            if nb == "end" {
                p2 += 1;
            } else if nb != "start" {
                let mut new_path = path.clone();
                let mut new_cond = cond;

                if !nb.chars().any(|c| c.is_uppercase()) {
                    if !path.contains(nb) {
                        new_path.insert(nb.to_string());
                    } else if path.contains(nb) && new_cond {
                        new_cond = false;
                    } else {
                        continue;
                    }
                }

                queue.push_back((nb.to_string(), new_path, new_cond));
            }
        }
    }

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
