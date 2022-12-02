use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() {
    let mut file = File::open("input.txt")
        .expect("File not found");

    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("Error while reading file");

    let opponent = HashMap::from([
        ("A", 1),
        ("B", 2),
        ("C", 3)
    ]);
    
    let player = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3)
    ]);

    // problem 1
    let mut score = 0;
    for line in data.lines() {
        let mut iter = line.split_whitespace();
        let a = iter.next().unwrap();
        let b = iter.next().unwrap();

        if opponent[a] == player[b] {
            score += 3;
        } else if (a == "A" && b == "Y") || (a == "B" && b == "Z") || (a == "C" && b == "X"){
            score += 6;
        }
        score += player[b];
    }

    // problem
    let mut score2 = 0;
    for line in data.lines() {
        let mut iter = line.split_whitespace();
        let a = iter.next().unwrap();
        let b = iter.next().unwrap();

        if b == "X" {
            score2 += 0;
            if a == "A" {
                score2 += player["Z"];
            } else if a == "B" {
                score2 += player["X"];
            } else {
                score2 += player["Y"];
            }
        } else if b == "Y" {
            score2 += 3;
            if a == "A" {
                score2 += player["X"];
            } else if a == "B" {
                score2 += player["Y"];
            } else {
                score2 += player["Z"];
            }
        } else {
            score2 += 6;
            if a == "A" {
                score2 += player["Y"];
            } else if a == "B" {
                score2 += player["Z"];
            } else {
                score2 += player["X"];
            }
        }
    }

    println!("P1: {}", score);
    println!("P2: {}", score2);
}
