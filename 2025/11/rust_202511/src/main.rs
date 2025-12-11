use std::collections::HashMap;
use std::fs::read_to_string;

fn dfs(nodes: &HashMap<&str, Vec<&str>>, cur_node: &str, goal_node: &str, p1: &mut u64) {
    // BC
    if cur_node == goal_node {
        *p1 += 1;
        return;
    }
    for node in nodes.get(cur_node).unwrap().iter() {
        dfs(nodes, node, goal_node, p1);
    }

    return;
}

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    let nodes: HashMap<&str, Vec<&str>> = lines
        .iter()
        .map(|line| {
            let splits = line.split_once(": ").unwrap();
            (splits.0, splits.1.split_whitespace().collect())
        })
        .collect();

    let mut p1: u64 = 0;
    dfs(&nodes, "you", "out", &mut p1);
    println!("Part One: {}", p1);
}
