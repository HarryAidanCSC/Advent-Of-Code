use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().filter(|line| line.len() > 0).collect();

    let idx = lines
        .iter()
        .enumerate()
        .filter(|(_, line)| line.contains("x"))
        .map(|(i, _)| i)
        .nth(0)
        .unwrap();

    let mut p1 = 0;
    for grid in &lines[idx..] {
        println!("{:?}", grid);
        let (dim, req) = grid.split_once(": ").unwrap();
        let (m, n) = dim
            .split_once('x')
            .map(|(x0, x1)| (x0.parse::<u32>().unwrap(), x1.parse::<u32>().unwrap()))
            .unwrap();
        let mn = m * n;
        let req = req
            .split_whitespace()
            .map(|x| x.parse::<u32>().unwrap() * 3)
            .sum::<u32>();
        println!("{} {} {}, {}", m, n, mn, req * 3);
        if req * 3 <= mn {
            p1 += 1;
        }
    }
    println!("Part One: {}", p1);
}
