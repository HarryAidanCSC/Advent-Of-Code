use ::std::mem::take;
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::fs::read_to_string;

fn dist(coords0: &Vec<i64>, coords1: &Vec<i64>) -> i64 {
    let xdis = coords0[0] - coords1[0];
    let ydis = coords0[1] - coords1[1];
    let zdis = coords0[2] - coords1[2];

    let cumul = (xdis.pow(2) + ydis.pow(2) + zdis.pow(2)) as f64;
    return cumul.sqrt() as i64;
}
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i64>> = file
        .lines()
        .map(|x| x.split(',').map(|y| y.parse::<i64>().unwrap()).collect())
        .collect();

    let mut distances = BinaryHeap::new();
    for (i, c0) in lines.iter().enumerate() {
        for (j, c1) in lines.iter().enumerate() {
            if j <= i {
                continue;
            }
            let d = dist(c0, c1);
            distances.push(Reverse((d, i, j)));
        }
    }

    let mut in_network: HashMap<usize, usize> = HashMap::new();
    let mut networks = vec![vec![0; 0]; 0];
    for i in 0..lines.len() {
        in_network.insert(i, i);
        networks.push(Vec::from([i]));
    }

    for _ in 0..1000 {
        let Some(Reverse((_d, i, j))) = distances.pop() else {
            panic!("");
        };
        let network0 = in_network.get(&i).unwrap().clone();
        let network1 = in_network.get(&j).unwrap().clone();

        // Drain into network 1
        let nodes = take(&mut networks[network1]);
        for n in &nodes {
            in_network.insert(*n, network0);
        }
        networks[network0].extend(nodes);
    }

    // P1
    let mut heap: BinaryHeap<_> = networks.iter().map(|v: &Vec<usize>| v.len()).collect();
    let p1: usize = (0..3).filter_map(|_| heap.pop()).product();
    println!("Part One: {}", p1);
}
