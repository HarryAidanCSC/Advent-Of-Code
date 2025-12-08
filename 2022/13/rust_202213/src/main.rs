use serde::Deserialize;
use std::cmp::Ordering;
use std::fs::read_to_string;
#[derive(Deserialize, Debug, Clone, PartialEq, Eq)]
#[serde(untagged)]
enum Packet {
    Num(u32),
    List(Vec<Packet>),
}

impl Ord for Packet {
    fn cmp(&self, other: &Self) -> Ordering {
        match (self, other) {
            (Packet::Num(a), Packet::Num(b)) => a.cmp(b),
            (Packet::List(a), Packet::List(b)) => a.cmp(b),
            (Packet::Num(a), Packet::List(_)) => Packet::List(vec![Packet::Num(*a)]).cmp(other),
            (Packet::List(_), Packet::Num(b)) => self.cmp(&Packet::List(vec![Packet::Num(*b)])),
        }
    }
}
impl PartialOrd for Packet {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn main() {
    let mut p1 = 0;

    let file = read_to_string("2022\\13\\input.txt").unwrap();
    let lines: Vec<&str> = file.lines().into_iter().filter(|x| x.len() > 0).collect();
    for i in (0..lines.len()).step_by(2) {
        let left: Packet = serde_json::from_str(lines[i]).unwrap();
        let right: Packet = serde_json::from_str(lines[i + 1]).unwrap();
        if left < right {
            p1 += (i / 2) as i32 + 1;
        }
    }
    println!("Part One: {}", p1)
}
