use std::{collections::HashMap, fs};

fn dfs(
    node: &str,
    children: &HashMap<String, Vec<String>>,
    sizes: &HashMap<String, i64>,
    globe_trotter: &mut HashMap<String, i64>,
) -> (i64, i64) {
    let mut cur_size = *sizes.get(node).unwrap_or(&0);
    let mut asu = 0;

    // Go through children
    if let Some(child_nodes) = children.get(node) {
        for child in child_nodes {
            let (child_score, p1p) = dfs(child, children, sizes, globe_trotter);
            asu += p1p;
            cur_size += child_score;
        }
    }

    //
    if cur_size <= 100000 {
        asu += cur_size;
    }
    globe_trotter.insert(node.to_string(), cur_size);
    return (cur_size, asu);
}

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines = file.lines();

    let mut stack: Vec<&str> = vec![];
    let mut dir_size: HashMap<String, i64> = HashMap::new();
    let mut children: HashMap<String, Vec<String>> = HashMap::new();

    for line in lines.skip(1) {
        if line.starts_with("$ cd") {
            let loc = &line[5..];
            if loc == ".." {
                stack.pop();
            } else {
                stack.push(loc);
            }
        } else if line.starts_with("$ ls") {
            continue;
        } else {
            let cur_dir: String = format!("/{}", stack.join("/"));
            if line.starts_with("dir") {
                let child: String = format!("{}/{}", cur_dir, &line[4..]).replace("//", "/");
                children.entry(cur_dir).or_default().push(child);
            } else {
                let (size, _file) = line.split_once(' ').unwrap();
                let size = size.parse::<i64>().unwrap();
                *dir_size.entry(cur_dir).or_default() += size;
            }
        }
    }

    // DFS
    let mut kitchen_sync: HashMap<String, i64> = HashMap::new();
    let (total_size, p1) = dfs("/", &children, &dir_size, &mut kitchen_sync);

    // P2
    let min_to_free = total_size - 40000000;
    let mut p2 = i64::MAX;
    for value in kitchen_sync.values() {
        if value >= &min_to_free && value < &p2 {
            p2 = *value;
        }
    }

    println!("Part One {}", p1);
    println!("Part Two {}", p2);
}
