use std::collections::{BTreeSet, HashMap, VecDeque};
use std::fs::read_to_string;
fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<(i64, i64)> = file
        .lines()
        .map(|line| {
            let s = line.split_once(',').unwrap();
            (s.0.parse::<i64>().unwrap(), s.1.parse::<i64>().unwrap())
        })
        .collect();

    let mut p1 = 0;
    for (x0, y0) in lines.iter() {
        for (x1, y1) in lines.iter() {
            let dx = x1.abs_diff(*x0) + 1;
            let dy = y1.abs_diff(*y0) + 1;
            let area = dx as u64 * dy as u64;
            p1 = p1.max(area);
        }
    }

    // P2
    let mut unique_x = BTreeSet::new();
    let mut unique_y = BTreeSet::new();
    for &(x, y) in &lines {
        unique_x.insert(x);
        unique_y.insert(y);
    }

    let sx: Vec<i64> = unique_x.into_iter().collect();
    let sy: Vec<i64> = unique_y.into_iter().collect();
    let x_map: HashMap<i64, usize> = sx.iter().enumerate().map(|(i, &v)| (v, i * 2)).collect();
    let y_map: HashMap<i64, usize> = sy.iter().enumerate().map(|(i, &v)| (v, i * 2)).collect();

    let wc = sx.len() * 2 + 1;
    let hc = sy.len() * 2 + 1;
    let mut grid = vec![vec![0u8; wc]; hc];

    let mut prev = lines[lines.len() - 1];
    for &curr in &lines {
        let prev_cx = *x_map.get(&prev.0).unwrap();
        let prev_cy = *y_map.get(&prev.1).unwrap();
        let curr_cx = *x_map.get(&curr.0).unwrap();
        let curr_cy = *y_map.get(&curr.1).unwrap();

        for y in prev_cy.min(curr_cy)..=prev_cy.max(curr_cy) {
            for x in prev_cx.min(curr_cx)..=prev_cx.max(curr_cx) {
                grid[y + 1][x + 1] = 1;
            }
        }
        prev = curr;
    }
    let mut queue = VecDeque::new();
    queue.push_back((0, 0));
    grid[0][0] = 2;

    const DELTAS: [(isize, isize); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

    while let Some((r, c)) = queue.pop_front() {
        for (dr, dc) in DELTAS {
            let nr = r as isize + dr;
            let nc = c as isize + dc;
            if nr >= 0 && nr < hc as isize && nc >= 0 && nc < wc as isize {
                let nr = nr as usize;
                let nc = nc as usize;
                if grid[nr][nc] == 0 {
                    grid[nr][nc] = 2;
                    queue.push_back((nr, nc));
                }
            }
        }
    }
    let grw = |col_idx: usize| -> i64 {
        if col_idx == 0 || col_idx == wc - 1 {
            return 0;
        }

        let map_idx = col_idx - 1;
        if map_idx % 2 == 0 {
            1
        } else {
            let i = map_idx / 2;
            sx[i + 1] - sx[i] - 1
        }
    };

    let grh = |row_idx: usize| -> i64 {
        if row_idx == 0 || row_idx == hc - 1 {
            return 0;
        }
        let map_idx = row_idx - 1;
        if map_idx % 2 == 0 {
            1
        } else {
            let i = map_idx / 2;
            sy[i + 1] - sy[i] - 1
        }
    };

    let mut psum = vec![vec![0i64; wc + 1]; hc + 1];
    for r in 0..hc {
        let h_real = grh(r);
        for c in 0..wc {
            let w_real = grw(c);
            let is_valid = grid[r][c] != 2;
            let cell_area = if is_valid { w_real * h_real } else { 0 };

            psum[r + 1][c + 1] = cell_area + psum[r][c + 1] + psum[r + 1][c] - psum[r][c];
        }
    }

    let mut p2 = 0;

    for (i, c1) in lines.iter().enumerate() {
        for c2 in lines.iter().skip(i + 1) {
            let width = (c1.0.abs_diff(c2.0)) + 1;
            let height = (c1.1.abs_diff(c2.1)) + 1;
            let target_area = width as u64 * height as u64;

            if target_area <= p2 {
                continue;
            }
            let cx1 = x_map[&c1.0] + 1;
            let cy1 = y_map[&c1.1] + 1;
            let cx2 = x_map[&c2.0] + 1;
            let cy2 = y_map[&c2.1] + 1;

            let r_min = cy1.min(cy2);
            let r_max = cy1.max(cy2);
            let c_min = cx1.min(cx2);
            let c_max = cx1.max(cx2);
            let actual_sum =
                psum[r_max + 1][c_max + 1] - psum[r_min][c_max + 1] - psum[r_max + 1][c_min]
                    + psum[r_min][c_min];

            if actual_sum as u64 == target_area {
                p2 = target_area;
            }
        }
    }

    println!("Part One: {}", p1);
    println!("Part Two: {}", p2);
}
