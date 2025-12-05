use std::collections::HashSet;
use std::fs;

fn get_vis_coords(trees: &Vec<i32>) -> HashSet<usize> {
    let mut hs = HashSet::new();
    let mut cur = -1;
    for (i, tree) in trees.iter().enumerate().rev() {
        if tree > &cur {
            hs.insert(i);
        }
        cur = cur.max(*tree);
        if cur == 9 {
            break;
        }
    }
    let mut cur = -1;
    for (i, tree) in trees.iter().enumerate() {
        if tree > &cur {
            hs.insert(i);
        }
        cur = cur.max(*tree);
        if cur == 9 {
            break;
        }
    }

    return hs;
}

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<Vec<i32>> = file
        .lines()
        .map(|x| x.chars().map(|v| v.to_digit(10).unwrap() as i32).collect())
        .collect();

    let n = lines[0].len();
    let mut tines = vec![vec![]; n];

    let mut visible = HashSet::new();

    for (i, line) in lines.iter().enumerate() {
        // R -> L pass
        let x_coords = get_vis_coords(line);
        for coord in x_coords {
            visible.insert((coord, i));
        }

        // Append to transposed matrix
        for (j, value) in line.iter().enumerate() {
            tines[j].push(*value);
        }
    }

    // Vertical pass
    for (i, tine) in tines.iter().enumerate() {
        let y_coords = get_vis_coords(tine);
        for coord in y_coords {
            visible.insert((i, coord));
        }
    }

    println!("Part One: {}", visible.len());
}
