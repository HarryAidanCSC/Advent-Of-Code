use std::collections::HashMap;
use std::fs::read_to_string;

fn dfs(nodes: &HashMap<&str, Vec<&str>>, cur_node: &str, goal_node: &str, p1: &mut u64) {
    if cur_node == goal_node {
        *p1 += 1;
        return;
    }
    for node in nodes.get(cur_node).unwrap().iter() {
        dfs(nodes, node, goal_node, p1);
    }

    return;
}

fn dfs2<'a>(
    nodes: &HashMap<&str, Vec<&'a str>>,
    cur_node: &'a str,
    goal_node: &str,
    fft: bool,
    dac: bool,
    cache: &mut HashMap<(&'a str, bool, bool), u64>,
) -> u64 {
    if cur_node == goal_node {
        return if fft && dac { 1 } else { 0 };
    }

    let state = (cur_node, fft, dac);
    if cache.contains_key(&state) {
        return *cache.get(&state).unwrap();
    }
    let mut paths = 0;

    for ne_node in nodes.get(cur_node).unwrap().iter() {
        let nfft = fft || *ne_node == "fft";
        let ndac = dac || *ne_node == "dac";
        paths += dfs2(&nodes, ne_node, "out", nfft, ndac, cache)
    }
    cache.insert(state, paths);
    return paths;
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

    let mut cache = HashMap::new();
    let p2 = dfs2(&nodes, "svr", "out", false, false, &mut cache);

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
