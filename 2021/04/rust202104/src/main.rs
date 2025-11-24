use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let file = fs::read_to_string("../../input.txt").unwrap();
    let lines: Vec<&str> = file.lines().collect(); 
    
    // Parse input
    let header: Vec<&str> = lines[0].split(',').collect();
    
    // Bingo cards
    type MyBingoPos = HashMap<String, (i32, i32)>;
    let mut bingo_scores: HashMap<i32, Vec<i32>> = HashMap::new();
    let mut bingo_poss: HashMap<i32, MyBingoPos> = HashMap::new();
    let mut bingo_unseen: HashMap<i32, HashSet<String>> = HashMap::new();
    let inital_bingo_scores = vec![5; 10];

    let mut i = 0;
    let mut n = 0;
    let mut bingo_pos = MyBingoPos::new();
    let mut unseen_values: HashSet<String> = HashSet::new();
    
    for line in &lines[2..]{
        if line.len() == 0 { 
            bingo_scores.insert(i, inital_bingo_scores.clone());
            bingo_poss.insert(i, bingo_pos);
            bingo_unseen.insert(i, unseen_values);

            bingo_pos = MyBingoPos::new();
            unseen_values = HashSet::new();
            i += 1;
            n = 0;
            continue;
        }
        let bingo_line: Vec<&str> = line.split_whitespace().collect();
        for (idx, value) in bingo_line.iter().enumerate(){
            bingo_pos.insert(value.to_string(),(idx as i32, n));
            unseen_values.insert(value.to_string());
        }
        n += 1;

    }
    bingo_scores.insert(i, inital_bingo_scores.clone());
    bingo_poss.insert(i, bingo_pos);
    bingo_unseen.insert(i, unseen_values);



    // Iterate through the header
    let mut winners_round: Vec<i32>= vec![];
    let mut winners_score: HashMap<i32, i32> = HashMap::new();

    for num in header.iter(){
        for key in bingo_poss.keys(){
            if winners_score.contains_key(key){ continue; }
            // 1. Remove from unseen values
            bingo_unseen.get_mut(key).unwrap().remove(*num);
            // 2. Update scores
            if let Some(cur_pos) = bingo_poss.get(key).and_then(|card| card.get(*num)){
                let x = cur_pos.0;
                let y = cur_pos.1 + 5;
                
                // Win condition
                if (bingo_scores.get(&key).unwrap()[x as usize] == 1) || (bingo_scores.get(&key).unwrap()[y as usize] == 1) {
                    let mut cur_score = 0;

                    for value in bingo_unseen.get(key).unwrap() {
                        cur_score += value.parse::<i32>().unwrap();
                    } 
                    cur_score *= num.parse::<i32>().unwrap();

                    winners_round.push(*key);
                    winners_score.insert(*key, cur_score);
                    continue;;
                }

                // // -1 from score of corresponding row/col
                bingo_scores.get_mut(&key).unwrap()[x as usize] -= 1;
                bingo_scores.get_mut(&key).unwrap()[y as usize] -= 1;
                
            }
        }
    }
    println!("Part One: {:?}", winners_score.get(&winners_round[0]).unwrap());
    println!("Part Two: {:?}", winners_score.get(&winners_round[winners_round.len() -1]).unwrap());
}