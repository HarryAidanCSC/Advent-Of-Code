use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect();

    // Starting items
    let mut items: Vec<Vec<i64>> = lines
        .iter()
        .filter_map(|x| {
            if x.contains("Starting items") {
                Some(
                    x.split_whitespace()
                        .skip(2)
                        .map(|s| s.trim_matches(',').parse::<i64>().unwrap())
                        .collect(),
                )
            } else {
                None
            }
        })
        .collect();

    // Operations
    let ops: Vec<&str> = lines
        .iter()
        .filter_map(|x| {
            if x.contains("Operation") {
                x.split(" = ").nth(1)
            } else {
                None
            }
        })
        .collect();

    let mut operations: Vec<Box<dyn Fn(i64) -> i64>> = vec![];
    for op in ops {
        let splits: Vec<&str> = op.split_whitespace().collect();
        let operator = splits[1];
        let operand = splits[2].parse::<i64>();

        let operation: Box<dyn Fn(i64) -> i64> = match operator {
            "+" => {
                if let Ok(num) = operand {
                    Box::new(move |old| old + num)
                } else {
                    Box::new(move |old| old + old)
                }
            }
            "*" => {
                if let Ok(num) = operand {
                    Box::new(move |old| old * num)
                } else {
                    Box::new(move |old| old * old)
                }
            }
            _ => panic!("Oof"),
        };
        operations.push(operation);
    }

    // Test
    let mut tests: Vec<Box<dyn Fn(i64) -> usize>> = vec![];
    for i in (3..lines.len()).step_by(7) {
        // Div value
        let div_val = lines[i]
            .split_whitespace()
            .last()
            .unwrap()
            .parse::<i64>()
            .unwrap();

        // True
        let true_cond = lines[i + 1]
            .split_whitespace()
            .last()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        let false_cond = lines[i + 2]
            .split_whitespace()
            .last()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        let fun = Box::new(move |x| {
            if x % div_val == 0 {
                true_cond
            } else {
                false_cond
            }
        });
        tests.push(fun);
    }

    // Do this thing
    let mut inspections = vec![0; tests.len()];
    for _ in 0..20 {
        for i in 0..items.len() {
            let current_items: Vec<i64> = items[i].drain(..).collect();
            inspections[i] += current_items.len() as i64;
            for worry in current_items {
                let new_worry = operations[i](worry) / 3;
                items[tests[i](new_worry)].push(new_worry);
            }
        }
    }

    inspections.sort();
    let p1: i64 = inspections.iter().rev().take(2).product();
    println!("Part One: {}", p1);
}
